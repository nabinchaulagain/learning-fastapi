import typing as ty

from fastapi import Depends, status
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from sqlalchemy.orm.session import Session

from animal.schemas import AnimalPayloadSchema, AnimalResponseSchema
from animal.services import AnimalService
from core.database import get_session

router = InferringRouter(tags=["animal"])


@cbv(router)
class AnimalView:

    service: AnimalService = Depends(AnimalService)

    @router.get("/animals", response_model=ty.List[AnimalResponseSchema])
    def get_all_animals(self, session: Session = Depends(get_session)):
        return self.service.fetch_all(session=session)

    @router.get("/animals/{id}", response_model=AnimalResponseSchema)
    def find_animal(self, id: int, session: Session = Depends(get_session)):

        return self.service.find_by_id(session=session, id=id)

    @router.post("/animals", response_model=AnimalResponseSchema)
    def add_animal(
        self,
        payload: AnimalPayloadSchema,
        session: Session = Depends(get_session),
    ):
        return self.service.create(session=session, payload=payload)

    @router.delete("/animals/{id}", status_code=status.HTTP_204_NO_CONTENT)
    def delete_animal(
        self,
        id: int,
        session: Session = Depends(get_session),
    ):
        self.service.delete(session=session, id=id)

    @router.patch("/animals/{id}", response_model=AnimalResponseSchema)
    def update_animal(
        self,
        payload: AnimalPayloadSchema,
        id: int,
        session: Session = Depends(get_session),
    ):
        return self.service.update(session=session, id=id, payload=payload)
