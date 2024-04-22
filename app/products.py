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


@app.get('/')  # mark the function as one processing requests
async def read_root():
    return {"message": "Hello World!2"}


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in sample_products:
        if product['product_id'] == product_id:
            return product
    return {"message" : "Product not found"}


app = FastAPI(title="PRODUCTS")


# @app.get("/product/search")
# def read_product_by_keyword(keyword: str, category: str = None, limit: int = 10):
#     if not category:
#         return list(filter(lambda x: keyword in x.name, map(lambda item: Product(**item),
#                            sample_products)))[:limit]
#     else:
#         return list(filter(
#             lambda x: keyword in x.name and x.category == category, map(
#                 lambda item: Product(**item), sample_products)))[:limit]


@app.get('/products/search')
async def get_products(keyword: str, category: str = None, limit: int = 10):
    res = []
    for prod in sample_products:
        if keyword in prod['name'] and (prod['category'] == category or category is None):
            res.append(prod)
    return res[:limit]

# uvicorn app.products:app --reload