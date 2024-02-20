#!/usr/bin/python3
""" export all users' data to json format """
import json
import requests


if __name__ == '__main__':
    return_j = {}
    save_j = {}
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    for i in users:
        u_id = i.get('id')
        return_j[u_id] = []
        save_j[u_id] = i.get('username')
    for i in todos:
        j_dict = {}
        u_id = i.get('userId')
        j_dict['task'] = i.get('title')
        j_dict['username'] = save_j.get(u_id)
        j_dict['completed'] = i.get('completed')
        return_j.setdefault(u_id, []).append(j_dict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(return_j, f)
