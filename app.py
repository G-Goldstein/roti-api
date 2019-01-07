from flask import Flask
from flask_restful import Api
from waitress import serve

app = Flask(__name__)
api = Api(app)

from cubes import CubesMock
from cube import CubeMock
api.add_resource(CubesMock, "/mock/cubes/")
api.add_resource(CubeMock, "/mock/cubes/<int:id>/")

from drafts import DraftsMock
from draft import DraftMock
from draft_picks import DraftPicksMock
api.add_resource(DraftsMock, "/mock/drafts/")
api.add_resource(DraftMock, "/mock/drafts/<int:id>/")
api.add_resource(DraftPicksMock, "/mock/drafts/<int:draft>/picks/<player>/")

serve(app, host='0.0.0.0', port='5000')