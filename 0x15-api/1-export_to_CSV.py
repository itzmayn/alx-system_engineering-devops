#!/usr/bin/python3
"""A Python script that returns information about an employee's TODO list progress."""
import json
import requests
import sys

def get_todo_info():
    """Function to retrieve and process TODO list progress for a given employee."""
    user_id = sys.argv[1]

    # Get user information based on the provided user ID
    user_response = requests.get('https://jsonplaceholder.typicode.com/users?id={}'.format(user_id))
    user_data = json.loads(user_response.text)
    user_name = user_data[0].get('username')

    # Get TODO list for the user
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    todos = json.loads(todos_response.text)

    # Create a dictionary to store the TODO list progress
    todo_dict = {}
    task_list = []

    # Iterate through each task in the TODO list
    for task in todos:
        task_data = {}
        task_data['task'] = task.get('title')
        task_data['completed'] = task.get('completed')
        task_data['username'] = user_name
        task_list.append(task_data)

    todo_dict[user_id] = task_list

    # Write the TODO list progress to a JSON file
    with open("{}.json".format(user_id), 'w', encoding='utf-8') as fp:
        json.dump(todo_dict, fp)

if __name__ == "__main__":
    get_todo_info()
