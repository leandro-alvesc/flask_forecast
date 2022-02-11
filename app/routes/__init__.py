from app.routes.forecast import forecast


def register_blueprints(app):
    app.register_blueprint(forecast, url_prefix='/forecast')
