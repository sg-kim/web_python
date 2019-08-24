import os

def getList():
	files = os.listdir('./15_form_CRUD_func/data')
	listStr = ''
	for item in files:
		listStr = listStr + '<li><a href="15_form_CRUD_func.py?id={name}">{name}</a></li>'.format(name=item)
	return listStr

