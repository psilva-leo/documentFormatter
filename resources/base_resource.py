from flask import make_response, render_template
from flask_restful import Resource

from parser.parser_chooser import ParserChooser


class BaseResource(Resource):

    def __init__(self, document_name: str):
        self._document_name = document_name
        self._parser = ParserChooser().get_parser(parser=document_name)

    def get(self):
        raise NotImplementedError('Child class must implement parse_data method')

    def post(self):
        raise NotImplementedError('Child class must implement parse_data method')

    def _render_template(self, **kwargs):
        headers = {'Content-Type': 'text/html'}

        return make_response(render_template(self._document_name + '.html', **kwargs), 200, headers)
