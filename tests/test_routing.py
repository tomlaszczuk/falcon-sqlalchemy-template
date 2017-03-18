import json
import falcon

from . import APITest
from api.routes import register_routes


class ExampleResource:

    def on_get(self, req, resp):
        resp.body = json.dumps({'message': 'test'})
        resp.status = falcon.HTTP_200


class RoutingTestCase(APITest):

    def setUp(self):
        super(RoutingTestCase, self).setUp()
        example = ExampleResource()
        example_routers = [
            ('/example/resource', example)
        ]
        other_routers = [
            ('/other/resource', example)
        ]
        self.registered_routes = [
            example_routers,
            other_routers
        ]

    def test_routing(self):
        register_routes(app=self.app, routes=self.registered_routes)

    def test_accessing_routed_endpoints(self):
        register_routes(app=self.app, routes=self.registered_routes)
        response = self.simulate_get('/example/resource')
        self.assertEqual(response.status, falcon.HTTP_200)
        response = self.simulate_get('/other/resource')
        self.assertEqual(response.status, falcon.HTTP_200)
