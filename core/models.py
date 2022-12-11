from sqlalchemy import Column, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import BigInteger, DateTime, String

from animal.choices import PhylumChoices

BaseModel = declarative_base()


class AuditedModel(BaseModel):  # type: ignore
    __abstract__ = True

    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime)


class Animal(AuditedModel):
    __tablename__ = "animal"

    id = Column("id", BigInteger, primary_key=True)
    name = Column("name", String, unique=True, nullable=False)
    phylum = Column("phylum", Enum(PhylumChoices), nullable=False)
