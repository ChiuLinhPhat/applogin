from fastapi import FastAPI
from api.routers.Auth import router as auth_router
from mongoengine import connect
from loguru import logger
app = FastAPI()


@app.on_event("startup")
async def create_db_client():
    try:
        connect(host="mongodb://127.0.0.1:27017/my_database")
        logger.info("Successfully connected to Mongo database.")
    except Exception as e:
        logger.error(e)
        logger.error("An error occurred while connecting to Mongo database.")
app.include_router(auth_router)