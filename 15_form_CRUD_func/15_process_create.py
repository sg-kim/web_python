#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi
form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

# store into a file
opened_file = open('./15_form_CRUD_func/data/' + title + '.txt', 'w')
opened_file.write(description)
opened_file.close()

# redirection
print("Location: 15_form_CRUD_func.py?id=" + title + '.txt')
print()

