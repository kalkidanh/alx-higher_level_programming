#!/bin/bash
#script that sends a request to a URL and displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
