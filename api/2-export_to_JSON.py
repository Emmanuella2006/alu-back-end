#!/usr/bin/python3
"""
Exports employee TODO list data to JSON format.
"""

import json
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]

    # Fetch user info
    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ) as response:
        user = json.loads(response.read().decode())

    username = user.get("username")

    # Fetch user tasks
    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    ) as response:
        todos = json.loads(response.read().decode())

    # Build JSON structure
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    final_data = {user_id: tasks_list}

    # Write to file
    filename = "{}.json".format(user_id)
    with open(filename, mode="w") as json_file:
        json.dump(final_data, json_file)
