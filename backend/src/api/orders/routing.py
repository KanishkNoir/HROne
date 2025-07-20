from fastapi import APIRouter, Query, Request
from .models import OrderCreate
from typing import Optional

router = APIRouter()

@router.post("/", status_code=201)
async def create_order(order: OrderCreate, request: Request):
    db = request.app.state.database
    result = await db.orders.insert_one(order.model_dump())
    return {"id": str(result.inserted_id)}

@router.get("/", status_code=200)
async def get_orders(
    request: Request,
    limit: int = Query(10, ge=1, description="Number of documents to return"),
    offset: int = Query(0, ge=0, description="Number of documents to skip while pagination")
):
    db = request.app.state.database
    
    cursor = db.orders.find({}).skip(offset).limit(limit)
    orders = []
    async for order in cursor:
        order["_id"] = str(order["_id"])
        orders.append(order)
    
    total_count = await db.orders.count_documents({})
    
    actual_limit = len(orders)
    next_page = offset + limit if offset + limit < total_count else None
    previous_page = offset - limit if offset > 0 else None
    
    return {
        "data": orders,
        "page": {
            "next": next_page,
            "limit": actual_limit,
            "previous": previous_page
        }
    }
