from datetime import datetime
from marshmallow import fields, validate
import app

from app.models import db, ma
from app.exceptions import BadRequest


class Forecast(db.Model):
    __tablename__ = 'forecast'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_city = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    country = db.Column(db.String(2), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    rain_probability = db.Column(db.Integer, nullable=False)
    rain_precipitation = db.Column(db.Integer, nullable=False)
    min_temperature = db.Column(db.Integer, nullable=False)
    max_temperature = db.Column(db.Integer, nullable=False)

    def __init__(self, id_city, city, state, country, date, rain_probability,
                 rain_precipitation, min_temperature, max_temperature):
        self.id_city = id_city
        self.city = city
        self.state = state
        self.country = country
        self.date = date
        self.rain_probability = rain_probability
        self.rain_precipitation = rain_precipitation
        self.min_temperature = min_temperature
        self.max_temperature = max_temperature


def validate_date(value):
    try:
        datetime.strptime(value, '%Y-%m-%d')
    except ValueError as err:
        message = str(err)
        app.logger.error(message)
        raise BadRequest({
            'code': 'BAD_REQUEST',
            'message': message
        })


class ForecastSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    id_city = fields.Int(required=True)
    city = fields.Str(required=True, validate=validate.Length(2, 30))
    state = fields.Str(required=True, validate=validate.Length(2, 2))
    country = fields.Str(required=True, validate=validate.Length(2, 2))
    date = fields.Str(required=True, validate=validate_date)
    rain_probability = fields.Int(
        required=True, validate=validate.Range(0, 100))
    rain_precipitation = fields.Int(required=True)
    min_temperature = fields.Int(required=True)
    max_temperature = fields.Int(required=True)


class CityIDSchema(ma.Schema):
    id = fields.Int(required=True)


class AnalysisSchema(CityIDSchema):
    init_date = fields.Str(required=True, validate=validate_date)
    end_date = fields.Str(required=True, validate=validate_date)


city_id_schema = CityIDSchema()
analysis_schema = AnalysisSchema()
forecast_schema = ForecastSchema()
partial_forecast_schema = ForecastSchema(partial=True)
forecasts_schema = ForecastSchema(many=True)
