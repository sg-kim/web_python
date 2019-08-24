#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi, os
form = cgi.FieldStorage()
title = form['title'].value

os.remove('./15_form_CRUD_func/data/' + title)

# redirection
print("Location: 15_form_CRUD_func.py")
print()

