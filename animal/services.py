from datetime import datetime

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.session import Session

from animal.constants import ANIMAL_NOT_FOUND_MESSAGE
from animal.schemas import AnimalPayloadSchema
from core.models import Animal


class AnimalService:
    def fetch_all(self, *, session: Session):
        return session.query(Animal).all()

    def create(self, *, session: Session, payload: AnimalPayloadSchema):
        """
        It creates an animal object, adds it to the database, and returns the animal object

        :param session: The database session
        :type session: Session
        :param payload: AnimalPayloadSchema
        :type payload: AnimalPayloadSchema
        :return: The animal object
        """
        animal = Animal(name=payload.name, phylum=payload.phylum)

        session.add(animal)
        try:
            session.commit()
        except IntegrityError:
            raise HTTPException(
                detail="An animal with the same name already exists",
                status_code=400,
            )

        session.refresh(animal)

        return animal

    def delete(self, *, session: Session, id: int):
        """
        It updates the `deleted_at` column of the `Animal` table with the current time.

        :param session: The SQLAlchemy session object
        :type session: Session
        :param id: The id of the animal to delete
        :type id: int
        """
        deleted_animal_count = (
            session.query(Animal)
            .filter(Animal.id == id)
            .update({"deleted_at": datetime.now()})
        )
        session.commit()

        if not deleted_animal_count:
            raise_name_not_unique_exception()

    def find_by_id(self, *, session: Session, id: int):
        """
        It takes an id, queries the database for an animal with that id, and returns the animal if it
        exists

        :param session: This is the SQLAlchemy session that we'll use to query the database
        :type session: Session
        :param id: The id of the animal to find
        :type id: int
        :return: The animal object
        """
        animal = session.query(Animal).filter(Animal.id == id).one_or_none()

        if animal is None:
            raise_not_found_exception()

        return animal

    def update(
        self, *, session: Session, payload: AnimalPayloadSchema, id: int
    ):
        """
        It updates an animal in the database

        :param session: The SQLAlchemy session object
        :type session: Session
        :param payload: AnimalPayloadSchema
        :type payload: AnimalPayloadSchema
        :param id: The id of the animal to update
        :type id: int
        :return: The animal object is being returned.
        """
        animal = self.find_by_id(session=session, id=id)

        animal.name = payload.name
        animal.phylum = payload.phylum

        session.add(animal)
        try:
            session.commit()
        except IntegrityError:
            raise_name_not_unique_exception()

        return animal


def raise_not_found_exception():
    raise HTTPException(status_code=404, detail=ANIMAL_NOT_FOUND_MESSAGE)


def raise_name_not_unique_exception():
    raise HTTPException(
        detail="An animal with the same name already exists",
        status_code=400,
    )


__all__ = ["AnimalService"]
