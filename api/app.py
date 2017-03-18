import os

import falcon

from api.config import config_dict
from api.db import SQLAlchemyMiddleware

from api.routes import register_routes, registered_routes


def create_app(environment_name):
    configuration = config_dict[environment_name]
    falcon_api = falcon.API(middleware=[
        SQLAlchemyMiddleware(configuration)
    ])
    register_routes(registered_routes, falcon_api)
    return falcon_api, configuration


api, config = create_app(os.getenv('APP_ENV') or 'default')
