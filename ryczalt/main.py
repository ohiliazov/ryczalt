from fastapi import FastAPI

from ryczalt.routers import debug


def create_app():
    app = FastAPI()
    app.include_router(debug.router)
    return app
