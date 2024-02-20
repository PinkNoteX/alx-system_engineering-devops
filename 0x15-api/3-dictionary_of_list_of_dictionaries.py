#!/usr/bin/python3
""" export data to json format """
import json
import requests
import sys


if __name__ == '__main__':
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    u_id = sys.argv[1]
    name = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(u_id)).json()
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(u_id)).json()
    j_dict = {}
    j_list = []
    for i in req:
        j_dict['task'] = i.get('title')
        j_dict['completed'] = i.get('completed')
        j_dict['username'] = i.get(name.get('username'))
        j_list.append(j_dict)
        j_dict = {}
    j_dict_r = {}
    j_dict_r[u_id] = j_list
    with open(u_id + '.json', 'w') as f:
        json.dump(j_dict_r, f)
