import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api


db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__)
    if test_config is None:
        # default database
        app.config['SQLALCHEMY_DATABASE_URI'] =\
                'sqlite:///database.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # FLASK_*
        app.config.from_prefixed_env()
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    api = Api(app)

    from .list import Lists, List, ListItems, ListItem
    api.add_resource(Lists, '/lists')
    api.add_resource(List, '/lists/<name>')
    api.add_resource(ListItems, '/lists/<name>/items')
    api.add_resource(ListItem, '/lists/<list_name>/items/<item_name>')

    return app
