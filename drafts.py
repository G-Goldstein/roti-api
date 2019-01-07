from flask_restful import Resource
import mock_drafts as md

MOCK = [
	md.draft
]

class DraftsMock(Resource):
	def get(self):
		return MOCK, 200