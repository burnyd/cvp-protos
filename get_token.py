#!/usr/bin/python3.6

import requests
import json
import grpc
import urllib3

CV_HOST = "10.20.30.185"
CV_API_PORT = "443"

USERNAME = "daniel"
PASSWORD = "daniel123"

r = requests.post('https://' + CV_HOST + '/cvpservice/login/authenticate.do', verify=False,
  auth=(USERNAME, PASSWORD))

print(r.json()['sessionId'])

with open("token.txt", "w") as f:
        f.write(r.json()['sessionId'])

channel_credentials = grpc.ssl_channel_credentials()
call_credentials = grpc.access_token_call_credentials(r.json()['sessionId'])
combined_credentials = grpc.composite_channel_credentials(channel_credentials, call_credentials)
channel = grpc.secure_channel(CV_HOST + ':' + CV_API_PORT, combined_credentials)
