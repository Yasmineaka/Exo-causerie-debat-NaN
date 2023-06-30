from flask import Blueprint



user_router=Blueprint('user_router', __name__, url_prefix='/api/user')
@user_router.get('/')