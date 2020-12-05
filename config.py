
from passwords import database_connection

SQLALCHEMY_DATABASE_URI_0 = database_connection

SQLALCHEMY_BINDS = {
    'cardchecker': SQLALCHEMY_DATABASE_URI_0,
}

SQLALCHEMY_TRACK_MODIFICATIONS = False

proxy_enabled = True


