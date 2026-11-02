#!/usr/bin/python3
"""Fetch an employee's TODO list progress from a REST API."""
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Print the TODO list progress for the given employee ID."""
    employee_id = int(sys.argv[1])
    user = requests.get(
        "{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(API_URL), params={"userId": employee_id}).json()

    done = [task for task in todos if task.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))


if __name__ == "__main__":
    main()
