from flask_restful import Resource

MOCK_1 = [
	{
		'name': 'Black Lotus',
		'oracle_id': '5089ec1a-f881-4d55-af14-5d996171203b',
		'img': 'https://img.scryfall.com/cards/normal/en/vma/4.jpg?1517813031'
	}
]

MOCK_2 = [
	{
		'name': 'Jace, the Mind Sculptor',
		'oracle_id': '7f77a84e-5a4b-4834-aefa-3cecc175ae8e',
		'img': 'https://img.scryfall.com/cards/normal/en/a25/62.jpg?1521725550'
	}
]

class CubeMock(Resource):
	def get(self, id):
		if id == 1:
			return MOCK_1, 200
		if id == 2:
			return MOCK_2, 200
		return 'Cube not found', 404