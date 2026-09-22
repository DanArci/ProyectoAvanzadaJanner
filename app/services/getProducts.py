from routes.router import router
from sqlmodel import Session, select
from models.Products import Products
from database import engine

@router.get("/products", summary="Get products with limit and skip by category and search")
def get_products(limit: int = 3, skip: int = 0, category: str = None, search: str = None):
    statement = select(Products)
    
    if category:
        statement = statement.where(Products.category == category)
    if search:
        statement = statement.where(Products.name.ilike(f"%{search}%"))

    statement = statement.offset(skip).limit(limit)

    with Session(engine) as session:
        return session.exec(statement).all()