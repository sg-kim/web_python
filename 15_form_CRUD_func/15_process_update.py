#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi, os
form = cgi.FieldStorage()
pageId = form['pageId'].value
title = form['title'].value
description = form['description'].value

# store into a file
opened_file = open('./15_form_CRUD_func/data/' + pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('./15_form_CRUD_func/data/' + pageId, './15_form_CRUD_func/data/' + title + '.txt')

# redirection
print("Location: 15_form_CRUD_func.py?id=" + title + '.txt')
print()

