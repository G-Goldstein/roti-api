from flask_restful import Resource
import mock_cards as mc
import mock_cubes

MOCK_1 = {
	'details': mock_cubes.power,
	'cards': [
		mc.ancestral_recall,
		mc.black_lotus,
		mc.mox_emerald,
		mc.mox_jet,
		mc.mox_pearl,
		mc.mox_ruby,
		mc.mox_sapphire,
		mc.time_walk,
		mc.timetwister,
	]
}

MOCK_2 = {
	'details': mock_cubes.martin,
	'cards': [
		mc.channel,
		mc.coalition_relic,
		mc.emrakul_the_aeons_torn,
		mc.grim_monolith,
		mc.griselbrand,
		mc.jace_the_mind_sculptor,
		mc.mother_of_runes,
		mc.recurring_nightmare,
		mc.umezawas_jitte,
		mc.wurmcoil_engine,
	]
}

class CubeMock(Resource):
	def get(self, id):
		if id == 1:
			return MOCK_1, 200
		if id == 2:
			return MOCK_2, 200
		return 'Cube not found', 404