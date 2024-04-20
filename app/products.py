from fastapi import FastAPI
from app.models.models import Product
from typing import Union


sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]

app = FastAPI()


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in sample_products:
        if product['product_id'] == product_id:
            return product
    return {"message" : "Product not found"}


@app.get("/products/search")
async def search_products(keyword: str, category: Union[str, None] = None, limit: int = 10):
    pass


# uvicorn app.products:app --reload