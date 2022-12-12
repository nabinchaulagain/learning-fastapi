from fastapi import HTTPException, status


class NotFoundException(HTTPException):
    def __init__(self, message):
        self.message = message
        self.status_code = status.HTTP_404_NOT_FOUND


class UniqueConstraintViolationException(HTTPException):
    def __init__(self, message):
        self.message = message
        self.status_code = status.HTTP_409_CONFLICT
