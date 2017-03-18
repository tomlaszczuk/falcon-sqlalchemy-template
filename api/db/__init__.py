from sqlalchemy import create_engine, orm


class SQLAlchemy:

    def __init__(self, conn_str):
        self.engine = create_engine(conn_str)
        self.session = None

    def connect(self):
        sm = orm.sessionmaker(bind=self.engine, autoflush=True,
                              autocommit=True, expire_on_commit=True)
        self.session = orm.scoped_session(sm)

    @staticmethod
    def close(session):
        session.flush()
        session.close()
        session.remove()


class SQLAlchemyMiddleware:

    def __init__(self, config):
        self.db = SQLAlchemy(config.SQLALCHEMY_DATABASE_URI)

    def process_resource(self, req, resp, resource, params):
        self.db.connect()
        resource.session = self.db.session

    def process_response(self, req, resp, resource, req_succeeded):
        if hasattr(resource, 'session'):
            self.db.close(resource.session)
