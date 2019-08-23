#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi
form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

# store into a file
opened_file = open('./13_form_delete/data/' + title + '.txt', 'w')
opened_file.write(description)
opened_file.close()

# redirection
print("Location: 13_form_delete.py?id=" + title + '.txt')
print()

