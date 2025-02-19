from fastapi import APIRouter
from controllers import *

api_router = APIRouter()
api_router.include_router(user_controller.router, prefix="/users", tags=["users"])
api_router.include_router(collect_controller.router, prefix="/collect", tags=["collect"])
api_router.include_router(post_controller.router, prefix="/posts", tags=['posts'])
api_router.include_router(product_category_controller.router, prefix="/product/categories", tags=['product'])
