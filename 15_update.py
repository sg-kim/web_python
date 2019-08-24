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
else:
	pageId = 'Welcome'
	description = 'The World Wide Web (abbrebiated WWW or the Web) is ...'

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
	<form action="15_process_update.py" method="post">
		<input type="hidden" name="pageId" value="{title}">
		<p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
		<p><textarea rows=4 name="description" placeholder="description">{form_default_description}</textarea></p>
		<p><input type="submit"></p>
	</form>
</body>
</html>
'''.format(listStr=view_15.getList(), title=pageId, desc=description, form_default_title=pageId, form_default_description=description))

