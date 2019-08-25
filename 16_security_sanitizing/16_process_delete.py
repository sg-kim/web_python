#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi, os
form = cgi.FieldStorage()
title = form['title'].value

os.remove('./16_security_sanitizing/data/' + title)

# redirection
print("Location: 16_security_sanitizing.py")
print()

