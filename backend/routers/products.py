from fastapi import APIRouter, HTTPException

router = APIRouter()

# Sample data
products = [
    {"id": 1, "name": "Product 1", "price": 100},
    {"id": 2, "name": "Product 2", "price": 200},
]

@router.get("/products")
async def get_all_products():
    return products

@router.get("/products/{product_id}")
async def get_product_by_id(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Not product found")
