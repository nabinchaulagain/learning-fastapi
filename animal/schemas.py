from pydantic import Field

from animal.choices import PhylumChoices
from core.schemas import BaseSchema


class AnimalResponseSchema(BaseSchema):
    id: int
    name: str
    phylum: PhylumChoices


class AnimalPayloadSchema(BaseSchema):
    name: str = Field(..., max_length=255, min_length=3)
    phylum: PhylumChoices
