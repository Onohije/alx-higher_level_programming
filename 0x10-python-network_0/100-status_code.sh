#!/bin/bash
# sends a request to a URL passed as an argument displays only the status code

curl -s -w '%{http_code}' "$1" -o /dev/null
