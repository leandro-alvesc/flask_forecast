import re
from datetime import datetime

import app
import requests
from app.exceptions import BadRequest, InternalServerError
from app.models import db
from app.models.forecast import Forecast, forecasts_schema
from sqlalchemy.exc import SQLAlchemyError


class ForecastController:
    @staticmethod
    def get_forecasts():
        forecasts = Forecast.query.all()
        return forecasts

    @classmethod
    def get_today_forecast_by_city_id(cls, id_city):
        today = datetime.now()
        forecast = {}
        try:
            app.logger.info('Searching in database...')
            forecast = Forecast.query.filter(
                Forecast.id_city == id_city,
                Forecast.date == today.strftime('%Y-%m-%d')).one()
        except SQLAlchemyError as e:
            app.logger.error(str(e))
            app.logger.error('Not found in database, creating new...')
            payload = cls.__get_forecasts_from_api(id_city)[0]
            forecast = cls.__insert_forecast(payload)
            cls.__commit_session()
        return forecast

    @classmethod
    def update_forecasts(cls, id_city):
        updated_forecasts = list()
        forecast_list = cls.__get_forecasts_from_api(id_city)

        dates = [fc.get('date') for fc in forecast_list]

        existent_forecasts = Forecast.query.filter(
            Forecast.id_city == id_city,
            Forecast.date.in_(dates)).all()

        # Update existent forecast if applicable
        for forecast in existent_forecasts:
            date_index = cls.__find_index_in_list(
                forecast_list, 'date', forecast.date)
            if date_index is not None:
                forecast_data = forecast_list.pop(date_index)
                forecast.date = forecast_data.get('date')
                updated_forecasts.append(forecast)

        # Create new forecasts
        new_forecasts = [cls.__insert_forecast(fc) for fc in forecast_list]
        cls.__commit_session()
        return {
            'new': forecasts_schema.dump(new_forecasts),
            'updated': forecasts_schema.dump(updated_forecasts)
        }

    @classmethod
    def __get_forecasts_from_api(cls, id):
        url = f'{app.config.CLIMA_TEMPO_URL}/forecast/locale/{id}/days/15'
        params = {'token': app.config.CLIMA_TEMPO_TOKEN}
        response = requests.get(url, params)

        if not response.ok:
            raise BadRequest({
                'code': 'BAD_REQUEST',
                'message': 'Invalid city ID'
            })
        response = response.json()

        forecast_list = list()

        for forecast in response.get('data'):
            forecast_rain = forecast.get('rain')
            forecast_temperature = forecast.get('temperature')

            payload = {
                'id_city': id,
                'city': response.get('name'),
                'state': response.get('state'),
                'country': response.get('country').split(' ')[0],
                'date': forecast.get('date'),
                'rain_probability': forecast_rain.get('probability'),
                'rain_precipitation': forecast_rain.get('precipitation'),
                'min_temperature': forecast_temperature.get('min'),
                'max_temperature': forecast_temperature.get('max'),
            }
            forecast_list.append(payload)
        return forecast_list

    @staticmethod
    def __insert_forecast(payload):
        forecast = Forecast(**payload)
        db.session.add(forecast)
        return forecast

    @classmethod
    def __commit_session(cls):
        try:
            db.session.commit()
        except SQLAlchemyError as e:
            app.logger.error(str(e))
            raise InternalServerError(cls.__format_error_message(e))

    @staticmethod
    def __format_error_message(err):
        message = str(err.__dict__['orig'])
        error_name = type(err.__dict__['orig']).__name__
        code = re.sub('([A-Z][a-z]+)', r' \1',
                      re.sub('([A-Z]+)', r' \1', error_name)).split()
        code = '_'.join(code)
        return {
            'code': code.upper(),
            'message': message
        }

    @staticmethod
    def __find_index_in_list(lst, key, value):
        for i, dic in enumerate(lst):
            if dic.get(key) == value:
                return i
        return None
