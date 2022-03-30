from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sendgrid import SendGridAPIClient
from os import environ

conexion = SQLAlchemy()
validador = Marshmallow()
sendgrid = SendGridAPIClient(api_key=environ.get('SENDGRID_API_KEY'))
