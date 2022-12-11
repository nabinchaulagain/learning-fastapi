from enum import Enum


class PhylumChoices(str, Enum):
    MOLLUSCA = "Mollusca"
    PORIFERA = "Porifera"
    CNIDARIA = "Cnidaria"
    PLATYHELMINTHES = "Platyhelminthes"
    NEMATODA = "Nematoda"
    ANNELIDA = "Annelida"
    ARTHROPODA = "Arthropoda"
    ECHINODERMATA = "Echinodermata"
    CHORDATA = "Chordata"


__all__ = ["PhylumChoices"]
