#!/usr/bin/python3
"""A Python script that fetches data from https://alx-intranet.hbtn.io/status
   and displays information about the response."""
import urllib.request


def main():
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as r:
        res = r.read()
        print('Body response:')
        print('\t- type: {}'.format(type(res)))
        print('\t- content: {}'.format(res))
        print('\t- utf8 content: {}'.format(res.decode('utf8')))


if __name__ == "__main__":
    main()
