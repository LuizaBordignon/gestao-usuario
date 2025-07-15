from routes.home import home_route
from routes.cliente import cliente_route
from database.database import db
from database.models import Cliente

def configure_all(app):
    configure_routes(app)

def configure_routes():
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')

def configure_db():
    db.connect()
    db.create_tables([Cliente])