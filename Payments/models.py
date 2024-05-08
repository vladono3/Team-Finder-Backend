from typing import Literal, List

from pydantic import BaseModel


class PriceFetch(BaseModel):
    price_id: str
    interval: str
    currency: str
    amount: int


class Pricing(BaseModel):
    name: str
    product_id: str
    description: str
    price_list: List[PriceFetch]


class Plan(BaseModel):
    price_id: str


class ClientSecret(BaseModel):
    client_secret: str
