from sqlmodel import Field, SQLModel
 
class Products(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(min_length=3)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    description: str | None = Field(default=None, max_length=200)
    category: str = Field(min_length=1)
    created_at: str
