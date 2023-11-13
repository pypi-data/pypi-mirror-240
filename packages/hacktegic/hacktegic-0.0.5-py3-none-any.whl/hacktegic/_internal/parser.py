import argparse

from hacktegic._internal.commands.auth.login import LoginCommand


class ArgumentParser(argparse.ArgumentParser):
    def __init__(self, **kwargs):
        super(ArgumentParser, self).__init__(**kwargs)

    def add_arguments(self):
        subparsers = self.add_subparsers()

        auth_parser = subparsers.add_parser("auth", help="authentication commands")
        auth_subparsers = auth_parser.add_subparsers(help="auth sub-command help")

        login_parser = auth_subparsers.add_parser("login", help="login help")
        login_parser.set_defaults(func=LoginCommand.run)

        logout_parser = auth_subparsers.add_parser("logout", help="logout help")
        # logout_parser.set_defaults(func=logout)

        register_parser = auth_subparsers.add_parser("register", help="register help")
        # register_parser.set_defaults(func=register)
