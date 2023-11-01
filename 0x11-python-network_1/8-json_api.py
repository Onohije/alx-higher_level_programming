#!/usr/bin/python3
"""A Python script that takes a letter as a command-line argument,
   sends an HTTP POST request to http://0.0.0.0:5000/search_user
   with the letter as a parameter, and processes the response."""

if __name__ == '__main__':
    import sys
    import requests
    import json

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) >= 2:
        char = sys.argv[1]
    else:
        char = ""

    data = {'q': char}
    r = requests.post(url, data=data)
    try:
        user = json.loads(r.text)
        print("[{}] {}".format(user['id'], user['name']))
    except KeyError:
        print("No result")
    except json.decoder.JSONDecodeError:
        print("Not a valid JSON")
