import argparse


class ArgsManager:
    def __init__(self) -> None:
        self.arguments = self.parse_arguments()

        self.host = self.arguments.host if self.arguments.host else "127.0.0.1"
        self.port = self.arguments.port if self.arguments.port else 5555
        self.key = self.arguments.key
        self.secret = self.arguments.secret
        self.environment = self.arguments.environment

        self.state = {
            "host": self.host,
            "port": self.port,
            "key": self.arguments.key,
            "secret": self.arguments.secret,
            "environment": self.arguments.environment,
        }

    def parse_arguments(self):
        try:
            parser = argparse.ArgumentParser()

            parser.add_argument("--host")
            parser.add_argument("--port")
            parser.add_argument("--environment")
            parser.add_argument("--key")
            parser.add_argument("--secret")

            return parser.parse_args()
        except Exception as e:
            print(e)


args_manager = ArgsManager()
