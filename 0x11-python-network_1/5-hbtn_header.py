#!/usr/bin/python3
"""A Python script that sends an HTTP GET request to a URL and displays
   the value of the 'X-Request-Id' variable found in the response headers."""

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
