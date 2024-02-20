#!/usr/bin/python3
""" export data to csv format """
import csv
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
    with open(u_id + '.csv', 'w', newline='') as cfile:
        write = csv.writer(cfile, quoting=csv.QUOTE_ALL)
        for i in req:
            write.writerow([name['id'], name['username'],
                            i['completed'], i['title']])
