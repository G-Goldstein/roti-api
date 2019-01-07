from flask_restful import Resource
import mock_drafts as md
import mock_cards as mc
import mock_players as mp

PICKS = {
	'john': [mc.jace_the_mind_sculptor],
	'graham': [mc.umezawas_jitte],
	'mike': [mc.recurring_nightmare],
	'adam': [mc.channel, mc.emrakul_the_aeons_torn],
	'martin': [mc.wurmcoil_engine, mc.coalition_relic]
}

class DraftPicksMock(Resource):
	def get(self, draft, player):
		if draft != 1:
			return 'Draft not found', 404
		if player not in PICKS:
			return 'Player not in draft', 404
		return {
			'draft': md.draft,
			'player': mp.players_dict[player],
			'picks': PICKS[player]
		}, 200