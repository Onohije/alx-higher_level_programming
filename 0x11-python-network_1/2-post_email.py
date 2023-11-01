#!/usr/bin/python3
"""A Python script that sends a POST request to a specified URL with an email
    parameter, and displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    import urllib.request
    import sys

    url, email = sys.argv[1:]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as r:
        print(r.read().decode('utf-8'))
