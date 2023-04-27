#!/bin/bash
# Script that uses curl to request a custom http header as an argument.
curl -s -H "X-School-User-Id: 98" "$1"
