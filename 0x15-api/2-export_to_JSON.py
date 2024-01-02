#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
from urllib import request
import requests
import sys
if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url+"users/{}".format(user_id)).json()
    username = user.get("username")
    todo = requests.get(url+"todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{"task": t.get("title"), "completed": t.get(
            "completed"), "username": username} for t in todo]}, jsonfile)
