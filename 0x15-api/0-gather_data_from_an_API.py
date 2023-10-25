#!/usr/bin/python3
"""Returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    # Base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get the user data based on the provided employee ID
    user = requests.get(base_url + "users/{}".format(argv[1])).json()

    # Get the TODO list for the user
    todos = requests.get(base_url + "todos", params={"userId": argv[1]}).json()

    # Extract completed tasks and store them in a list
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Display the employee's TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
          len(completed), len(todos)))

    # Print the titles of completed tasks
    [print("\t {}".format(com)) for com in completed]
