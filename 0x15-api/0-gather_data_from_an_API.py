#!/usr/bin/python3
""" return information based on id """
import requests
import sys


if __name__ == '__main__':
    NUMBER_OF_DONE_TASKS = 0
    TASK_TITLE = []
    u_id = sys.argv[1]
    req = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                       .format(u_id)).json()
    EMPLOYEE_NAME = req.get('name')
    req = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                       .format(u_id)).json()
    for i in req:
        if i.get('completed') is True:
            TASK_TITLE.append(i.get('title'))
            NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS = len(req)
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for t in TASK_TITLE:
        print('\t {}'.format(t))
