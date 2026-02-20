from fastapi import FastAPI
from app.routers import text_router

app = FastAPI()

app.include_router(text_router.router)

@app.get("/")
def health_check():
    return {"status": "ok"}

