#!/usr/bin/env python3

import storeonce_api
import sys
import xmltodict
import json

sapi=storeonce_api.StoreOnceAPI(endpoint='https://172.26.4.119',login='zabbix_test',password='zabbix_test')
#sapi.timeout=20
print(json.dumps(xmltodict.parse(sapi.get.status(route=sys.argv[1]))))
exit(0)



