#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi
form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

# store into a file
opened_file = open('./16_security_sanitizing/data/' + title + '.txt', 'w')
opened_file.write(description)
opened_file.close()

# redirection
print("Location: 16_security_sanitizing.py?id=" + title + '.txt')
print()

