from flask import Flask, render_template, request
from parser.parser_chooser import ParserChooser


def create_app():
    app = Flask(__name__)
    print('Application started!')

    @app.route('/')
    def index():
        return json()

    @app.route('/json.html', methods=['GET', 'POST'])
    def json():

        parser = ParserChooser().get_parser(parser='json')

        json_data = []
        if request.method == 'POST':
            request_data = request.form.to_dict(flat=False)
            print(request_data)
            json_data = parser.parse_data(data=request_data)
        return render_template('json.html', json_data=json_data)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)
