from flask import Blueprint
from flask_restful import Api
from resources.json_resource import JsonResource

json_blueprint = Blueprint('json_page', __name__, template_folder='templates')
json_api = Api(json_blueprint, prefix='/json.html', default_mediatype='text/html')

json_api.add_resource(JsonResource, '/', strict_slashes=False, endpoint='json')
