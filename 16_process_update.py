#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi, os
form = cgi.FieldStorage()
pageId = form['pageId'].value
title = form['title'].value
description = form['description'].value

# store into a file
opened_file = open('./16_security_sanitizing/data/' + pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('./16_security_sanitizing/data/' + pageId, './16_security_sanitizing/data/' + title + '.txt')

# redirection
print("Location: 16_security_sanitizing.py?id=" + title + '.txt')
print()

