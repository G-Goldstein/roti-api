from flask import Flask
from flask_restful import Api
from waitress import serve
from resources import add_resources

app = Flask(__name__)
api = Api(app)

add_resources(api)

serve(app, host='0.0.0.0', port='5000')