from flask_restful import Resource
import mocks.drafts as md

MOCK = [
	md.draft
]

class DraftsMock(Resource):
	def get(self):
		return MOCK, 200