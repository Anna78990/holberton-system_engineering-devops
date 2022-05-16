#!/usr/bin/python3
"""
   Write a Python script that, using this REST API, for a given employee ID,
   and extend the Python script to export data in the JSON format.
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
    uj = users.json()
    tj = tasks.json()

    len_u = len(uj)
    d = {}
    for u in range(0, len_u):
        d_value = []
        for i in tj:
            if i['userId'] == uj[u]['id']:
                d_value.append({"username": uj[u]['username'],
                                "task": i['title'],
                                "completed": i['completed']})
        d[uj[u]['id']] = d_value
    json_file = open('todo_all_employees.json', 'w')
    json.dump(d, json_file)
