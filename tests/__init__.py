import os

from falcon import testing
from api.app import create_app
from api import db

from sqlalchemy_utils import database_exists, create_database, drop_database

from alembic import command
from alembic.config import Config


class APITest(testing.TestCase):

    @classmethod
    def setUpClass(cls):
        super(APITest, cls).setUpClass()
        app, config = create_app('TESTING')
        cls.DATABASE_URI = config.SQLALCHEMY_DATABASE_URI

        if not database_exists(cls.DATABASE_URI):
            create_database(cls.DATABASE_URI)
        alembic_cfg = Config(os.path.join(config.PROJECT_ROOT, 'alembic.ini'))
        alembic_cfg.set_main_option(
            'script_location',
            os.path.join(config.PROJECT_ROOT, 'migrations')
        )
        alembic_cfg.set_main_option(
            'sqlalchemy.url', config.SQLALCHEMY_DATABASE_URI
        )

        command.upgrade(alembic_cfg, 'head')

    def setUp(self):
        super(APITest, self).setUp()
        self.app, self.config = create_app('TESTING')

    @classmethod
    def tearDownClass(cls):
        drop_database(cls.DATABASE_URI)

    def connect_db(self):
        self.db_session = db.SQLAlchemy(
            self.config.SQLALCHEMY_DATABASE_URI
        ).connect()

    def close_db(self):
        db.SQLAlchemy.close(session=self.db_session)
