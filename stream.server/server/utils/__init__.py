from functools import wraps, partial

from flask_restful import reqparse

BodyArg = partial(reqparse.Argument, location="json", required=True)


def validate(*arguments):
    def parse(func):
        @wraps(func)
        def resource(*args, **kwargs):
            parser = reqparse.RequestParser()
            for arg in arguments:
                parser.add_argument(arg)
            return func(*args, **{**kwargs, **parser.parse_args()})
        return resource
    return parse
