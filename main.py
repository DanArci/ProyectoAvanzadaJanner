from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    id: int
    price: float
    category: str
    stock: int

products = [
    Product(name="Teclado", id=1, price=10.99, category="A", stock=100),
    Product(name="Mouse", id=2, price=15.99, category="B", stock=50),
    Product(name="Monitor", id=3, price=20.99, category="C", stock=25),
    Product(name="Laptop", id=4, price=5.99, category="A", stock=200),
    Product(name="Tablet", id=5, price=12.99, category="B", stock=75)
]

@app.get("/health")
def get_health():
    return {"status": "ok"}


@app.get("/")
def get_shop_info():
    return {"name": "My Shop", "version": "1.0.0", "total_products": len(products)}

    
@app.get("/products")
def get_products(limit: int = 3, skip: int = 0, category: str = None, search: str = None):
    filtered_products = products
    if category:
        filtered_products = [
            product for product in products 
                if product.category == category
        ]
    if search:
        filtered_products = [
            product for product in filtered_products
                if search.lower() in product.name.lower()
        ]
    return filtered_products[skip : skip+limit]

  
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")