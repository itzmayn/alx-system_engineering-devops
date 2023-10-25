#!/usr/bin/python3
"""
Python script that, using this REST API

"""

if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    ids = set()
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = r.json()
    for user in data:
        ids.add(user.get('userId'))

    output = {}
    for user in ids:
        r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(user))
        username = r.json().get('username')

        r = requests.get('https://jsonplaceholder.typicode.com/' +
                         'todos?userId={}'.format(user))
        data = r.json()

        output['{}'.format(user)] = []
        for task in data:
            output['{}'.format(user)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': username
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump({int(x): output[x] for x in output.keys()},
                  file, sort_keys=True)