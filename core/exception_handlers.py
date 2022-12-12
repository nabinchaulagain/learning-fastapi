import traceback

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from core.exceptions import (
    NotFoundException,
    UniqueConstraintViolationException,
)


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(NotFoundException)
    def not_found_exception_handler(
        request: Request, exception: NotFoundException
    ):
        return JSONResponse(
            {"message": exception.message},
            status_code=status.HTTP_404_NOT_FOUND,
        )

    @app.exception_handler(UniqueConstraintViolationException)
    def unique_constraint_violation_exception_handler(
        request: Request, exception: UniqueConstraintViolationException
    ):
        return JSONResponse(
            {"message": exception.message},
            status_code=status.HTTP_409_CONFLICT,
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request, e: Exception):
        response = {
            "message": f"An unexpected error occurred: {e}",
            "stackTrace": traceback.format_exc(),
        }

        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=response
        )
