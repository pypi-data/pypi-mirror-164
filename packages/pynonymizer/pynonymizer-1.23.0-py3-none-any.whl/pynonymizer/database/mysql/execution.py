import shutil
import shlex
import subprocess
from pynonymizer.database.exceptions import DependencyError

"""
Seperate everything that touches actual query exec into its own module
"""


class MySqlDumpRunner:
    def __init__(
        self, db_host, db_user, db_pass, db_name, db_port="3306", additional_opts=""
    ):
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        self.db_port = db_port
        self.additional_opts = shlex.split(additional_opts)

        if not (shutil.which("mysqldump")):
            raise DependencyError(
                "mysqldump", "The 'mysqldump' client must be present in the $PATH"
            )

    def __get_base_params(self):
        return [
            "--host",
            self.db_host,
            "--port",
            self.db_port,
            "--user",
            self.db_user,
            f"-p{self.db_pass}",
        ]

    def open_dumper(self):
        return subprocess.Popen(
            ["mysqldump"]
            + self.__get_base_params()
            + self.additional_opts
            + [self.db_name],
            stdout=subprocess.PIPE,
        ).stdout


class MySqlCmdRunner:
    def __init__(
        self, db_host, db_user, db_pass, db_name, db_port="3306", additional_opts=""
    ):
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        self.db_port = db_port
        self.additional_opts = shlex.split(additional_opts)
        self.process = None

        if not (shutil.which("mysql")):
            raise DependencyError(
                "mysql", "The 'mysql' client must be present in the $PATH"
            )

    def __mask_subprocess_error(self, error):
        """
        messes with the internals of a CalledProcessError to hide the fact that there's a password in there,
        in case it bubbles out in a traceback.

        This might be better as a wrapping exception, rather than messing around inside other people's classes.
        """
        error.cmd = [
            "mysql",
            "-h",
            self.db_host,
            "-P",
            self.db_port,
            "-u",
            self.db_user,
            "-p******",
        ]
        raise error from None

    def __get_base_params(self):
        return [
            "mysql",
            "-h",
            self.db_host,
            "-P",
            self.db_port,
            "-u",
            self.db_user,
            f"-p{self.db_pass}",
        ]

    def execute(self, statements):
        if not isinstance(statements, list):
            statements = [statements]

        outputs = []

        for statement in statements:
            try:
                outputs.append(
                    subprocess.check_output(
                        self.__get_base_params()
                        + self.additional_opts
                        + ["--execute", statement]
                    )
                )
            except subprocess.CalledProcessError as error:
                self.__mask_subprocess_error(error)

        return outputs

    def db_execute(self, statements):
        if not isinstance(statements, list):
            statements = [statements]

        outputs = []

        for statement in statements:
            try:
                outputs.append(
                    subprocess.check_output(
                        self.__get_base_params()
                        + self.additional_opts
                        + [self.db_name, "--execute", statement]
                    )
                )
            except subprocess.CalledProcessError as error:
                self.__mask_subprocess_error(error)

        return outputs

    def get_single_result(self, statement):
        try:
            return subprocess.check_output(
                self.__get_base_params()
                + ["-sN", *self.additional_opts, self.db_name, "--execute", statement]
            ).decode()
        except subprocess.CalledProcessError as error:
            self.__mask_subprocess_error(error)

    def open_batch_processor(self):
        self.close_batch_processor()
        self.process = subprocess.Popen(
            self.__get_base_params() + self.additional_opts + [self.db_name],
            stdin=subprocess.PIPE,
        )
        return self.process.stdin

    def close_batch_processor(self):
        if self.process is not None:
            self.process.stdin.close()
            self.process.wait()
            self.process = None
