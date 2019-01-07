from flask_restful import Resource
import mocks.cubes as mcu

MOCK = [
	mcu.power,
	mcu.martin
]

class CubesMock(Resource):
	def get(self):
		return MOCK, 200