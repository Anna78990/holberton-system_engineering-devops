#!/usr/bin/python3
import json
import requests
import sys

args = sys.argv
n = args[1]

users = requests.get('https://jsonplaceholder.typicode.com/users')
tasks = requests.get('https://jsonplaceholder.typicode.com/todos')
uj = users.json()
tj = tasks.json()

person = uj[int(n)-1]['name']
all = 0
done = 0
cmt_list = []

for i in tj:
    if i['userId'] == int(n):
        all += 1
        if i['completed'] is True:
            done += 1
            cmt_list.append(i['title'])
print('Employee {} is done with tasks({}/{}):'.format(person, done, all))
for i in cmt_list:
    print('\t{}'.format(i))
