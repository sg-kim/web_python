#!/usr/bin/python3
print("Content-Type: text/html")
print()
print('Hello web')

import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
if pageId:
	pageId = pageId
else:
	pageId = 'WEB'

#	docstring
print('''<!doctype html>
<html>
<head>
	<title>WEB - Welcome</title>
	<meta charset="utf-8">
</head>
<body>
	<h1><a href="04_url_query_string.py">WEB</a></h1>
	<ol>
		<li><a href="04_url_query_string.py?id=HTML">HTML</a></li>
		<li><a href="04_url_query_string.py?id=CSS">CSS</a></li>
		<li><a href="04_url_query_string.py?id=JavaScript">JavaScript</a></li>
	</ol>
	<h2>{title}</h2>
	<p>The World Wide Web (abbrebiated WWW or the Web) is ...
	</p>
</body>
</html>
'''.format(title=pageId))

