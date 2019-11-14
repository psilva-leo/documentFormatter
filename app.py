from flask import Flask, render_template
from flask_material import Material


def create_app():
    app = Flask(__name__)
    Material(app)
    print('Application started!')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)
