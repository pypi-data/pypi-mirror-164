from flask import Blueprint
sm_blue = Blueprint('sm', __name__, url_prefix='/smapi')
from . import views