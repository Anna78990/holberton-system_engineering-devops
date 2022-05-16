#!/usr/bin/python3
"""
   Write a Python script that, using this REST API, for a given employee ID,
   and extend the Python script to export data in the CSV format.
"""
import json
import requests
import sys
import csv

args = sys.argv
n = args[1]

"""
   to make the elements be inside doublequote
"""
class CustomFormat(csv.excel):
    quoting = csv.QUOTE_ALL


users = requests.get('https://jsonplaceholder.typicode.com/users')
tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
uj = users.json()
tj = tasks.json()
id = uj[int(n)-1]['id']
person = uj[int(n)-1]['username']
rows = []
csv_file = open('{}.csv'.format(id), 'w', newline='')
writer = csv.writer(csv_file, dialect=CustomFormat(),)
for i in tj:
    if i['userId'] == int(n):
        rows.append((id, person, i['completed'], i['title']))
writer.writerows(rows)

csv_file.close()
