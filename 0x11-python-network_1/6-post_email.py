#!/usr/bin/python3
"""A Python script that sends an HTTP POST request to a
   URL with an email parameter, and displays the body of the response."""

if __name__ == "__main__":
    import requests
    import sys

    url, email = sys.argv[1:]
    data = {'email': email}

    r = requests.post(url, data=data)
    print(r.text)
