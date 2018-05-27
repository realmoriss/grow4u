import os
from flask import Flask, render_template


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    from . import db
    db.init_app(app)

    from . import datalog
    app.register_blueprint(datalog.bp)

    return app