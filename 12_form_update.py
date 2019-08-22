#!/usr/bin/python3
print("Content-Type: text/html")
print()
print('Hello web')

import cgi, os

files = os.listdir('./12_form_update/data')
listStr = ''
for item in files:
	listStr = listStr + '<li><a href="12_form_update.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
	pageId = form["id"].value
	description = open('./12_form_update/data/' + pageId, 'r').read()
	update_link = '<a href="12_update.py?id={}">update</a>'.format(pageId)
else:
	pageId = 'Welcome'
	description = 'The World Wide Web (abbrebiated WWW or the Web) is ...'
	update_link = ''

#	docstring
print('''<!doctype html>
<html>
<head>
	<title>WEB - Welcome</title>
	<meta charset="utf-8">
</head>
<body>
	<h1><a href="12_form_update.py">WEB</a></h1>
	<ol>{listStr}</ol>
	<a href="12_create.py">create</a>
	{update_link}
	<h2>{title}</h2>
	<p>{desc}</p>
</body>
</html>
'''.format(listStr=listStr, title=pageId, desc=description, update_link=update_link))

