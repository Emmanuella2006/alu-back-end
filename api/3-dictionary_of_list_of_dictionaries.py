#!/usr/bin/python3
"""
Exports all employees' TODO list data to JSON format.
"""

import json
import urllib.request


if __name__ == "__main__":

    # Fetch all users
    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users"
    ) as response:
        users = json.loads(response.read().decode())

    # Fetch all todos
    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/todos"
    ) as response:
        todos = json.loads(response.read().decode())

    # Build a dictionary of userId -> username
    user_dict = {}
    for user in users:
        user_dict[user["id"]] = user["username"]

    # Build final structure
    final_data = {}

    for todo in todos:
        user_id = str(todo["userId"])

        if user_id not in final_data:
            final_data[user_id] = []

        final_data[user_id].append({
            "username": user_dict[todo["userId"]],
            "task": todo["title"],
            "completed": todo["completed"]
        })

    # Write to file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(final_data, json_file)
