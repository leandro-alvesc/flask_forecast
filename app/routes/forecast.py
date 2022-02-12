from app.controllers.forecast import ForecastController
from app.decorators import Decorators as Dec
from app.models.forecast import (analysis_schema, city_id_schema,
                                 forecast_schema, forecasts_schema)
from flask import Blueprint, jsonify

forecasts = Blueprint('forecast', __name__)


@forecasts.route('', methods=['GET'])
def get_forecasts():
    forecasts = ForecastController.get_forecasts()
    return jsonify(forecasts_schema.dump(forecasts))


@forecasts.route('/analysis', methods=['GET'])
@Dec.required_schema(analysis_schema)
def forecast_analysis(body, *args, **kwargs):
    analysis = ForecastController.analysis_forecasts()
    return jsonify(analysis)


@forecasts.route('/city', methods=['GET'])
@Dec.required_schema(city_id_schema)
def get_forecast(body, **kwargs):
    id = body.get('id')
    today_forecast = ForecastController.get_today_forecast_by_city_id(id)
    return jsonify(forecast_schema.dump(today_forecast))


@forecasts.route('/city/sync', methods=['GET'])
@Dec.required_schema(city_id_schema)
def sync_forecasts(body, **kwargs):
    id = body.get('id')
    return jsonify(ForecastController.update_forecasts(id))
