from flask_restful import Resource
import mocks.cards as mc
import mocks.cubes as mcu

MOCK_1 = {
	'details': mcu.power,
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
	'details': mcu.martin,
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