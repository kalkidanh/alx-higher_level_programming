#!/bin/bash
# Script that takes a URL as an argument and displays the allowed http methods
curl -s -I "$1" | grep "Allow" | cut -d " " -f 2-
