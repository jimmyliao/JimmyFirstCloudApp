from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.routers import chat, healthcheck, products
from fastapi import FastAPI

app = FastAPI()

app.include_router(chat.router, prefix="/api")
app.include_router(healthcheck.router, prefix="/api")
app.include_router(products.router, prefix="/api")

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
