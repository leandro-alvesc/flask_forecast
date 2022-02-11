from flask import Blueprint, jsonify
from app.controllers.forecast import ForecastController

from app.models.forecast import forecasts_schema

forecast = Blueprint('forecast', __name__)


@forecast.route('', methods=['GET'])
def get_forecasts():
    forecasts = ForecastController.get_forecasts()
    return jsonify(forecasts_schema.dump(forecasts))
