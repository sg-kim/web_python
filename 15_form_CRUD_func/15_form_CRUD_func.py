#!/usr/bin/python3
print("Content-Type: text/html")
print()
print('Hello web')

import cgi, os, view_15

'''
files = os.listdir('./15_form_CRUD_func/data')
listStr = ''
for item in files:
	listStr = listStr + '<li><a href="15_form_CRUD_func.py?id={name}">{name}</a></li>'.format(name=item)
'''

form = cgi.FieldStorage()
if 'id' in form:
	pageId = form["id"].value
	description = open('./15_form_CRUD_func/data/' + pageId, 'r').read()
	update_link = '<a href="15_update.py?id={}">update</a>'.format(pageId)
	delete_action = '''
		<form action="15_process_delete.py" method="post">
			<input type="hidden" name="title" value="{}">
			<input type="submit" value="delete">
		</form>
	'''.format(pageId)
else:
	pageId = 'Welcome'
	description = 'The World Wide Web (abbreviated WWW or the Web) is ...'
	update_link = ''
	delete_action = ''

#	docstring
print('''<!doctype html>
<html>
<head>
	<title>WEB - Welcome</title>
	<meta charset="utf-8">
</head>
<body>
	<h1><a href="15_form_CRUD_func.py">WEB</a></h1>
	<ol>{listStr}</ol>
	<a href="15_create.py">create</a>
	{update_link}
	{delete_action}
	<h2>{title}</h2>
	<p>{desc}</p>
</body>
</html>
'''.format(listStr=view_15.getList(), title=pageId, desc=description, update_link=update_link, delete_action=delete_action))

