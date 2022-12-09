from fastapi import FastAPI


class App:
    def __init__(self):
        self.server = FastAPI()


def run_server() -> FastAPI:
    app = App()

    return app.server
