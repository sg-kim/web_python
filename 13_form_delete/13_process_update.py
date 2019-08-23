#!/usr/bin/python3
#print("Content-Type: text/html")
#print()

import cgi, os
form = cgi.FieldStorage()
pageId = form['pageId'].value
title = form['title'].value
description = form['description'].value

# store into a file
opened_file = open('./13_form_delete/data/' + pageId, 'w')
opened_file.write(description)
opened_file.close()

os.rename('./13_form_delete/data/' + pageId, './13_form_delete/data/' + title + '.txt')

# redirection
print("Location: 13_form_delete.py?id=" + title + '.txt')
print()

