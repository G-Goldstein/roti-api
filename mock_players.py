# Our IDs have come from our order in the rotisserie draft.

john = {
	'id': 'john',
	'name': 'John'
}

graham = {
	'id': 'graham',
	'name': 'Graham'
}

mike = {
	'id': 'mike',
	'name': 'Mike'
}

adam = {
	'id': 'adam',
	'name': 'Adam'
}

martin = {
	'id': 'martin',
	'name': 'Martin'
}

players = [john, graham, mike, adam, martin]

players_dict = {
	p['id']:p for p in players
}