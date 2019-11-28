from flask import request

from resources.base_resource import BaseResource


class JsonResource(BaseResource):

    def __init__(self):
        super().__init__(document_name='json')

    def get(self):
        json_data = []
        return self._render_template(json_data=json_data)

    def post(self):
        request_text = self._get_text()
        formatted_json = self._parser.parse_data(data=request_text)

        return self._render_template(json_data=formatted_json)
