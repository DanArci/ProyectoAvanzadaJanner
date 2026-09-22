from routes.router import router
from sqlmodel import Session
from models.Products import Products
from database import engine
from schemas.ProductInputSchemas import ProductInputSchema
from datetime import datetime
from fastapi import HTTPException

@router.post("/products", summary="Post products with models",)
def post_products(product : ProductInputSchema):

    with Session(engine) as session:
        db_product = Products(
            created_at=datetime.now().isoformat(),
            **product.model_dump(),
        )

        # El id se genera automatico al colocarlo en la bd
        session.add(db_product)
        session.commit()
        session.refresh(db_product)
        raise HTTPException(status_code=201, detail="Product succesfully added")