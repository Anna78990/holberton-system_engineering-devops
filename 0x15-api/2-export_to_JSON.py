#!/usr/bin/python3
"""
   Write a Python script that, using this REST API, for a given employee ID,
   and extend the Python script to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    args = sys.argv
    n = args[1]

    users = requests.get('https://jsonplaceholder.typicode.com/users')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    uj = users.json()
    tj = tasks.json()
    id = uj[int(n)-1]['id']
    person = uj[int(n)-1]['username']
    d_value = []
    for i in tj:
        if i['userId'] == int(n):
            d_value.append({"task": i['title'], "completed": i['completed'],
                           "username": person})
    j = {n: d_value}
    json_file = open('{}.json'.format(n), 'w')
    json.dump(j, json_file)
