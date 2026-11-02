#!/usr/bin/python3
"""Export an employee's TODO list to a CSV file."""
import csv
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com"


def main():
    """Write all tasks of the given employee to USER_ID.csv."""
    employee_id = int(sys.argv[1])
    user = requests.get(
        "{}/users/{}".format(API_URL, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(API_URL), params={"userId": employee_id}).json()
    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username,
                             task.get("completed"), task.get("title")])


if __name__ == "__main__":
    main()
