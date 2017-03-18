import json

import falcon
from sqlalchemy_utils import database_exists

from . import APITest
from api.db import SQLAlchemy


class DBExistsTestCase(APITest):

    def test_db_exists(self):
        self.assertTrue(database_exists(self.config.SQLALCHEMY_DATABASE_URI))


class ExampleResource:

    def on_get(self, req, resp):
        resp.body = json.dumps({'message': 'test',
                                'session': repr(self.session)})
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        del self.session
        resp.status = falcon.HTTP_200


class SQLAlchemyConnectionTestCase(APITest):

    def test_creating_connection(self):
        db = SQLAlchemy(self.config.SQLALCHEMY_DATABASE_URI)
        self.assertIsNone(db.session)
        db.connect()
        self.assertIsNotNone(db.session)

    def test_closing_connection(self):
        db = SQLAlchemy(self.config.SQLALCHEMY_DATABASE_URI)
        db.connect()
        db.close(db.session)


class SQLAlchemyMiddlewareTestCase(APITest):

    def test_connection_accessed_from_endpoints(self):
        example = ExampleResource()
        self.app.add_route('/example', example)
        response = self.simulate_get('/example')
        self.assertEqual(response.status, falcon.HTTP_200)

    def test_session_is_removed_in_endpoint(self):
        example = ExampleResource()
        self.app.add_route('/example', example)
        response = self.simulate_post('/example')
        self.assertEqual(response.status, falcon.HTTP_200)
