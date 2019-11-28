import time

from flask import make_response, render_template, g, request
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
        elapsed_time = self._get_elapsed_time()

        return make_response(render_template(self._document_name + '.html', elapsed_time=elapsed_time, **kwargs),
                             200, headers)

    @staticmethod
    def _get_elapsed_time():
        if request.method == 'POST':
            return "{0:.4f}".format(time.time() - g.start_time)

        return None

    def _get_text(self):
        request_data = request.form.to_dict(flat=False)
        request_text = request_data[self._document_name + '-textarea'][0]

        return request_text
