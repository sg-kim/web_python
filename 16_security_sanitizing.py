#!/usr/bin/python3
print("Content-Type: text/html")
print()
print('Hello web')

import cgi, os, view_16, html_sanitizer

'''
files = os.listdir('./16_security_sanitizing/data')
listStr = ''
for item in files:
	listStr = listStr + '<li><a href="16_security_sanitizing.py?id={name}">{name}</a></li>'.format(name=item)
'''

'''
from html_sanitizer import Sanitizer
sanitizer = Sanitizer();
'''
sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
	pageId = form["id"].value
	title = pageId
	description = open('./16_security_sanitizing/data/' + pageId, 'r').read()
	description = sanitizer.sanitize(description)
	title = sanitizer.sanitize(title)
	update_link = '<a href="16_update.py?id={}">update</a>'.format(pageId)
	delete_action = '''
		<form action="16_process_delete.py" method="post">
			<input type="hidden" name="title" value="{}">
			<input type="submit" value="delete">
		</form>
	'''.format(pageId)
else:
	pageId = 'Welcome'
	title = pageId
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
	<h1><a href="16_security_sanitizing.py">WEB</a></h1>
	<ol>{listStr}</ol>
	<a href="16_create.py">create</a>
	{update_link}
	{delete_action}
	<h2>{title}</h2>
	<p>{desc}</p>
</body>
</html>
'''.format(listStr=view_16.getList(), title=title, desc=description, update_link=update_link, delete_action=delete_action))

