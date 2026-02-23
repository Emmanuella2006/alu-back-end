#!/usr/bin/python3
"""Gather data from an API and display TODO list progress."""
import urllib.request
import json
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = base_url + "/users/" + str(employee_id)
    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())

    todos_url = base_url + "/todos?userId=" + str(employee_id)
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    name = user.get("name")
    done = [t for t in todos if t.get("completed")]
    total = len(todos)

    print("Employee " + name + " is done with tasks(" +
          str(len(done)) + "/" + str(total) + "):")
    for task in done:
        print("\t " + task.get("title"))
