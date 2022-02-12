import unittest

from app import app
from app import db


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self._ctx = self.app.test_request_context()
        self._ctx.push()

        db.create_all()

        self.city_id = 3477

        self.forecasts = self.client.get('/forecasts')
        self.today_forecast = self.client.get(
            f'/forecasts/city?id={self.city_id}')
        self.sync_forecast = self.client.get(
            f'/forecasts/city/sync?id={self.city_id}')

    def test_get_forecasts(self):
        print(self.forecasts.json)
        self.assertEqual(200, self.forecasts.status_code)

    def test_get_today_forecast(self):
        self.assertEqual(200, self.today_forecast.status_code)

    def test_sync_forecast(self):
        self.assertEqual(200, self.sync_forecast.status_code)
