from fastapi import APIRouter, Query, Request
from .models import ProductCreate
from typing import Optional

router = APIRouter()

@router.post("/", status_code=201)
async def create_product(product: ProductCreate, request: Request):
    db = request.app.state.database
    result = await db.products.insert_one(product.model_dump())
    return {"id": str(result.inserted_id)}

@router.get("/", status_code=200)
async def get_products(
    request: Request,
    name: Optional[str] = Query(None, description="Filter by name"),
    size: Optional[str] = Query(None, description="Filter by size"),
    limit: int = Query(10, ge=1, description="Number of documents to return"),
    offset: int = Query(0, ge=0, description="Number of documents to skip")
):
    db = request.app.state.database
    
    filter_dict = {}
    if name:
        filter_dict["name"] = {"$regex": name, "$options": "i"}
    if size:
        filter_dict["sizes.size"] = size
    
    cursor = db.products.find(filter_dict).skip(offset).limit(limit)
    products = []
    async for product in cursor:
        product["_id"] = str(product["_id"])
        products.append(product)
    
    total_count = await db.products.count_documents(filter_dict)

    actual_limit = len(products)
    next_page = offset + limit if offset + limit < total_count else None
    previous_page = offset - limit if offset > 0 else None
    
    return {
        "data": products,
        "page": {
            "next": next_page,
            "limit": actual_limit,
            "previous": previous_page
        }
    }