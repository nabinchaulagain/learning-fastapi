from fastapi import FastAPI

from animal.views import router as animal_router
from core import constants


class App:
    def __init__(self):
        self.server = FastAPI()
        self.include_routers()

    def get_routers(self):
        return [animal_router]

    def include_routers(self):
        for router in self.get_routers():
            self.server.include_router(
                router=router, prefix=constants.V1_API_BASE_PATH
            )


def run_server() -> FastAPI:
    app = App()

    return app.server
