from app.controllers.forecast import ForecastController
from app.models.forecast import forecasts_schema, forecast_schema
from app.decorators import Decorators as Dec
from flask import Blueprint, jsonify

forecasts = Blueprint('forecast', __name__)


@forecasts.route('', methods=['GET'])
def get_forecasts():
    forecasts = ForecastController.get_forecasts()
    return jsonify(forecasts_schema.dump(forecasts))


@forecasts.route('/city', methods=['GET'])
@Dec.required_id
def get_forecast(data, **kwargs):
    id = data.get('id')
    today_forecast = ForecastController.get_today_forecast_by_city_id(id)
    return jsonify(forecast_schema.dump(today_forecast))
