#!/bin/bash
# Script that takes a URL as an argument and returns the number of bytes in the body
# of the response.
curl -s "$1" | wc -c
