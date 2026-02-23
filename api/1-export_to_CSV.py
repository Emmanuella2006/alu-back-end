#!/usr/bin/python3
"""
Exports employee TODO list data to CSV format.
"""

import csv
import json
import sys
import urllib.request


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]

    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    ) as response:
        user = json.loads(response.read().decode())

    username = user.get("username")

    with urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id
        )
    ) as response:
        todos = json.loads(response.read().decode())

    filename = "{}.csv".format(user_id)

    with open(filename, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

