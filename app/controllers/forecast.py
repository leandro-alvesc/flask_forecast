from app.models.forecast import Forecast


class ForecastController:
    @staticmethod
    def get_forecasts():
        forecasts = Forecast.query.all()
        return forecasts
