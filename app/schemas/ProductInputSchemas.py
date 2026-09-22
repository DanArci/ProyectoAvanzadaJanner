from pydantic import BaseModel
from sqlmodel import Field

class ProductInputSchema(BaseModel):
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    category: str = Field(min_length=1)
    stock: int = Field(ge=0)
    description: str | None = Field(default=None, max_length=200)