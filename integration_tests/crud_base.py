from fastapi import APIRouter, HTTPException, Depends 
from integration_tests.dao import ProductDAO
from integration_tests.auth import authenticate_user
from integration_tests.models import Product, User


router = APIRouter(
    prefix="/access", 
    tags=["database"]
)


@router.get("/get_product")
async def get_product(name: str, user: User = Depends(authenticate_user)) -> list[Product]: 
    product = await ProductDAO.get_product(name=name) 
    if not product: 
        raise HTTPException(status_code=404) 
    return product 


@router.post("/add_product")
async def add_product(product: Product, user: User = Depends(authenticate_user)): 
    await ProductDAO.add_product(name=product.name, price=product.price)
    return {"message": "Done!"}


@router.put("/change_product")
async def change_product(name: str, price: float, user: User = Depends(authenticate_user)): 
    await ProductDAO.update_product(name=name, price=price)
    return {"message": "Done!"}


@router.delete("/delete_product")
async def delete_product(name: str, user: User = Depends(authenticate_user)): 
    await ProductDAO.delete_product(name=name) 
    return {"message": "Done!"}
