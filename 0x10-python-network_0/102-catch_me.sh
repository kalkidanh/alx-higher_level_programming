#!/bin/bash
# Script that makes a DNS request and fetches a stored message.
curl -s -L -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
