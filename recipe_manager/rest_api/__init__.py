""" REST api section of the application.

The REST api exposes interactions with the database.
"""
# pylint: disable=wrong-import-position

from flask.blueprints import Blueprint


rest_api_v1 = Blueprint("rest_api_v1", __name__)

from . import controller
