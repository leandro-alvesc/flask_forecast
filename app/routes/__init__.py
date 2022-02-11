from app.routes.forecast import forecasts


def register_blueprints(app):
    app.register_blueprint(forecasts, url_prefix='/forecasts')
