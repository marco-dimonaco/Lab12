from dataclasses import dataclass
from model.retailer import Retailer


@dataclass
class Connessione:
    rc1: Retailer
    rc2: Retailer
    n: int
