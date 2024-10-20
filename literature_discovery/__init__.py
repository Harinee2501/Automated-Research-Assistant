from flask import Blueprint

literature_discovery_bp=Blueprint('literature_discovery',__name__)

from . import views