from flask import Flask
from flask_restful import Api
from waitress import serve

from cubes import CubesMock
from cube import CubeMock

app = Flask(__name__)
api = Api(app)

api.add_resource(CubesMock, "/mock/cubes")
api.add_resource(CubeMock, "/mock/cubes/<int:id>")

serve(app, host='0.0.0.0', port='5000')