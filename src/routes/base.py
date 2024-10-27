from fastapi import FastAPI, APIRouter, Depends
from src.helpers.config import get_settings, settings

base_router= APIRouter(
    prefix='/api/v1',
    tags=['api_v1'],
)

@base_router.get("/")
async def welcome(app_settings : settings = Depends(get_settings) ):
    
    app_name = app_settings.APP_NAME
    app_version = app_settings.APP_VERSION
    return {
        "app_name":app_name,
        "app_version":app_version,
    }