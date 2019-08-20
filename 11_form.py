#!/usr/bin/python3
print("Content-Type: text/html")
print()
print('Hello web')

import cgi, os

files = os.listdir('./11_form/data')
listStr = ''
for item in files:
	listStr = listStr + '<li><a href="11_form.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
	pageId = form["id"].value
	description = open('./11_form/data/' + pageId, 'r').read()
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
	<h1><a href="10_article_list.py">WEB</a></h1>
	<ol>{listStr}</ol>
	<a href="11_form.py">create</a>
	<form action="11_process_create.py" method="post">
		<p><input type="text" name="title" placeholder="title"></p>
		<p><textarea rows=4 name="description" placeholder="description"></textarea></p>
		<p><input type="submit"></p>
	</form>
</body>
</html>
'''.format(listStr=listStr, title=pageId, desc=description))

