#!/usr/bin/python3
print("Content-Type: text/html")
print()
print('Hello web')

import cgi, os

files = os.listdir('./13_form_delete/data')
listStr = ''
for item in files:
	listStr = listStr + '<li><a href="13_form_delete.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
	pageId = form["id"].value
	description = open('./13_form_delete/data/' + pageId, 'r').read()
	update_link = '<a href="13_update.py?id={}">update</a>'.format(pageId)
	delete_action = '''
		<form action="13_process_delete.py" method="post">
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
	<h1><a href="13_form_delete.py">WEB</a></h1>
	<ol>{listStr}</ol>
	<a href="13_create.py">create</a>
	{update_link}
	{delete_action}
	<h2>{title}</h2>
	<p>{desc}</p>
</body>
</html>
'''.format(listStr=listStr, title=pageId, desc=description, update_link=update_link, delete_action=delete_action))

