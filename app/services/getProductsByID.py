from routes.router import router
from sqlmodel import Session, select
from models.Products import Products
from database import engine
from fastapi import HTTPException

@router.get("/products/{product_id}", summary="Get product by id")
def get_product(product_id: int):

    with Session(engine) as session:
        statement = select(Products).where(Products.id == product_id)
        product = session.exec(statement).first()
        if product : return product

    raise HTTPException(status_code=404, detail="Product not found")