#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi, os
form = cgi.FieldStorage()
title = form['title'].value

os.remove('./13_form_delete/data/' + title)

# redirection
print("Location: 13_form_delete.py")
print()

