from resources.cubes import CubesMock
from resources.cube import CubeMock

from resources.drafts import DraftsMock
from resources.draft import DraftMock
from resources.draft_picks import DraftPicksMock

def add_resources(api):
	
	api.add_resource(CubesMock, "/mock/cubes/")
	api.add_resource(CubeMock, "/mock/cubes/<int:id>/")

	api.add_resource(DraftsMock, "/mock/drafts/")
	api.add_resource(DraftMock, "/mock/drafts/<int:id>/")
	api.add_resource(DraftPicksMock, "/mock/drafts/<int:draft>/picks/<player>/")