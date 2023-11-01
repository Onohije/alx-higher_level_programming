#!/usr/bin/python3
"""A Python script that sends a POST request to a URL with an email parameter,
   and then displays the body of the response (decoded in utf-8)."""


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print('Error code: {}'.format(e.code))
