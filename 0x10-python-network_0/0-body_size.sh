#!/bin/bash
# Takes in, sends a request to that URL, and displays the size
curl -s "$1" | wc -c
