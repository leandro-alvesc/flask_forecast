from functools import wraps

from flask import jsonify, request
from flask_marshmallow import Schema
from marshmallow import ValidationError

import app


class Decorators:
    @staticmethod
    def required_schema(schema: Schema):
        def _required_schema(f):
            @wraps(f)
            def __required_schema(*args, **kwargs):
                body = request.json
                params = request.args

                if not isinstance(body, dict) and not len(params):
                    return {'code': 'required_schema'}, 400

                data = body or params

                try:
                    load_schema = schema.load(data)
                    return f(body=load_schema, *args, **kwargs)
                except ValidationError as err:
                    app.logger.error(err.messages)
                    return jsonify(err.messages), 400

            return __required_schema
        return _required_schema
