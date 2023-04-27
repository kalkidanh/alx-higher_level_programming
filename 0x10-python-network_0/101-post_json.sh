#!/bin/bash
# Script that sends a POST request to a URL using a JSON file.
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
