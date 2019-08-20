#!/usr/bin/python3
print("Content-Type: text/html")
print()
print('Hello web')

import cgi, os

files = os.listdir('./10_article_list/data')
print(files)

listStr = ''
for item in files:
	listStr = listStr + '<li><a href="10_article_list.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
	pageId = form["id"].value
	description = open('./10_article_list/data/' + pageId + '.txt', 'r').read()
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
	<a href="11_create.py">create</a>
	<h2>{title}</h2>
	<p>{desc}</p>
</body>
</html>
'''.format(listStr=listStr, title=pageId, desc=description))

