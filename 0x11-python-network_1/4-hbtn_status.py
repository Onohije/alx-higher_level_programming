#!/usr/bin/python3
"""A Python script that makes an HTTP GET request to fetch data from
https://alx-intranet.hbtn.io/status using the 'requests' library."""

if __name__ == '__main__':
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
