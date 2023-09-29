#!/usr/bin/python3
"""A Python script that sends an HTTP GET request to a URL,
retrieves the response, and displays the body of the response if the
status code is 200 (OK), otherwise it prints an error message."""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)

    if r.status_code == 200:
        print(r.text)
    else:
        print('Error code: {}'.format(r.status_code))
