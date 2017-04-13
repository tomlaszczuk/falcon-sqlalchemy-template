"""
# Routing idea for large projects:

# In your project modules put routes in routes.py as a list of mappings.
# Example.

# api/modules/users/routes.py

# Let's assume you have your resources classes in endpoints.py file

from . import endpoints

users_collection = endpoints.Collection()
users_detail = endpoints.Detail()

routes = [
    ('/users/{user_id}', users_detail),
    ('/users', users_collection)
]

# Import those routes here

from api.modules.users import routes as user_routes
from api.modules.another_module import routes as another_routes
# ...

put those routes in registered_routes list

registered_routes = [
    user_routes,
    another_routes
]

"""

from api.modules.pets.routes import routes as pet_routes


registered_routes = [
    pet_routes
]


def register_routes(routes, app):
    for module in routes:
        for route in module:
            app.add_route(route[0], route[1])
