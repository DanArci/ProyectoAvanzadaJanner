from routes.router import router
from sqlmodel import Session, select
from models.Products import Products
from database import engine

@router.get("/", summary="Shop Info")
def get_shop_info():
    with Session(engine) as session:
        statement = select(Products)
        products = session.exec(statement).all()
        total_products = len(products)
        return {"name": "My Shop", "version": "1.0.0", "total_products": total_products}