from flask import Flask, url_for, render_template
from blueprints import json_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(json_blueprint.json_blueprint)

    @app.route('/', methods=['GET'])
    def index():
        return render_template(url_for('json_page.json'))

    print('Application started!')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)
