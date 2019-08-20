#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi
form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

# store into a file
opened_file = open('./11_form/data/' + title + '.txt', 'w')
opened_file.write(description)

# redirection
print("Location: 11_form.py?id=" + title + '.txt')
print()

