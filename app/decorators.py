from functools import wraps

from flask import request


class Decorators:
    @staticmethod
    def required_id(f):
        @wraps(f)
        def _required_id(*args, **kwargs):
            body = request.json
            params = request.args

            if not isinstance(body, dict) and not len(params):
                return {'code': 'REQUIRED_DATA'}, 400

            data = body or params

            if 'id' not in data:
                return {'code': 'REQUIRED_ID'}, 400
            return f(data=data, *args, **kwargs)
        return _required_id
