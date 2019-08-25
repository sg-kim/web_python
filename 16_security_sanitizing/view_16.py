import os, html_sanitizer

def getList():
	sanitizer = html_sanitizer.Sanitizer()
	files = os.listdir('./16_security_sanitizing/data')
	listStr = ''
	for item in files:
		item = sanitizer.sanitize(item)
		listStr = listStr + '<li><a href="16_security_sanitizing.py?id={name}">{name}</a></li>'.format(name=item)
	return listStr

