import os
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from .api.products.routing import router as products_router
from .api.orders.routing import router as orders_router

client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))

app = FastAPI()

app.state.database = client.hrone_database

@app.on_event("startup")
async def startup_event():
    pass

@app.on_event("shutdown")
async def shutdown_event():
    if client:
        client.close()
        print("Disconnected from MongoDB")

app.include_router(products_router, prefix="/api/products")
app.include_router(orders_router, prefix="/api/orders")

@app.get("/")
def read_root():
    return {"message": "Hello welcome to the backend assignment by HROne submitted by Kanishk Pratap Singh"}