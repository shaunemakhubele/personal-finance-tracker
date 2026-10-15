
import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.environ.get(
            "SECRET_KEY",
            "local-development-key-change-before-deployment",
        ),
        DATABASE=os.path.join(app.instance_path, "finance.db"),
    )

    if test_config:
        app.config.update(test_config)

    os.makedirs(app.instance_path, exist_ok=True)

    from app.db import init_db
    init_db(app)

    from app.routes import main
    app.register_blueprint(main)

    return app
