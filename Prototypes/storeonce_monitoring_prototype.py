#!/usr/bin/env python3

import urllib.parse
import requests
from requests.auth import HTTPBasicAuth
import xmltodict
import json
import sys

requests.packages.urllib3.disable_warnings()

API_TIMEOUT = 15
API_METHOD_URL = "https://172.26.4.119/"+sys.argv[1]
LOGIN='zabbix_test'
PASSWORD='zabbix_test'

try:
    sapi = requests.get(API_METHOD_URL, verify=False,auth=HTTPBasicAuth(LOGIN, PASSWORD),timeout=API_TIMEOUT)
    sapi.raise_for_status()
#    d = json.loads(json.dumps(xmltodict.parse(sapi.text)))
    d = json.dumps(xmltodict.parse(sapi.text))
    print(d)

except Exception as inst:
    print(str(inst))
finally:
    exit(0)