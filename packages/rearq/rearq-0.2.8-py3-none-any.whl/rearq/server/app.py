import os

from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.staticfiles import StaticFiles

from .. import ReArq, constants
from .routes import router


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rearq = None

    def set_rearq(self, rearq: ReArq):
        self.rearq = rearq


app = App(title="API docs of ReArq")
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(constants.STATIC_DIR, "rearq", "server", "static")),
    name="static",
)
app.include_router(router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"msg": exc.detail},
    )
