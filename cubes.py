from flask_restful import Resource
import mock_cubes

MOCK = [
	mock_cubes.power,
	mock_cubes.martin
]

class CubesMock(Resource):
	def get(self):
		return MOCK, 200