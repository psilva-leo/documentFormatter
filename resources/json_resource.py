from typing import Tuple

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
        indent, sort_keys = self._get_parameters()

        formatted_json, error = self._parser.parse_data(data=request_text, indent=indent, sort_keys=sort_keys)

        return self._render_template(formatted_json=formatted_json, error=error)

    @staticmethod
    def _get_parameters() -> Tuple[int, bool]:
        request_data = request.form.to_dict(flat=False)
        minify = request_data['minify'] if 'minify' in request_data.keys() else None
        indent = None if minify else int(request_data['indent'][0])

        sort_keys = True if 'sort_keys' in request_data.keys() else False

        return indent, sort_keys
