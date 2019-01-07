from flask_restful import Resource
import mocks.drafts as md
import mocks.cards as mc
import mocks.players as mp

MOCK = {
	'details': md.draft,
	'players': mp.players,
	'next_pick': mp.mike,
	'remaining_cards': [mc.griselbrand, mc.mother_of_runes, mc.grim_monolith]
}

class DraftMock(Resource):
	def get(self, id):
		if id == 1:
			return MOCK, 200
		return 'Draft not found', 404