#!/usr/bin/env python3

"""

Мониторинг StoreOnce 5200 девайсов.

Использование:

LLD (возвращает Json с найденными шарама для Zabbix):
./storeonce_monitoring_main.py 172.26.4.119

Формирование json файла для получения данных:
./storeonce_monitoring_main.py 172.26.4.119 receive

Получение параметра userBytes для шары YouTrack:
./storeonce_monitoring_main.py 172.26.4.119 getdata YouTrack userBytes

"""

import requests
from requests.auth import HTTPBasicAuth
import xmltodict
import json
import traceback
import sys
import os

requests.packages.urllib3.disable_warnings()

path_repo="/tmp/hp_storeonce/"

def do_request(host=None):
    try:
        if host is not None:
            API_ENDPOINT_MONITORING="storeonceservices/cluster/servicesets/1/services/nas/shares"
            LOGIN='zabbix_test'
            PASSWORD='zabbix_test'
            API_TIMEOUT = 15
            API_METHOD_URL = "https://"+host+"/"+API_ENDPOINT_MONITORING
            sapi = requests.get(API_METHOD_URL, verify=False,auth=HTTPBasicAuth(LOGIN, PASSWORD),timeout=API_TIMEOUT)
            sapi.raise_for_status()
            return json.loads(json.dumps(xmltodict.parse(sapi.text)))
        else:
            return None

    except Exception as inst:
        print(traceback.format_exc())


def lld_mode(host=None):
    try:
        result={'data':[]}
        if host is not None:
            data=do_request(host)
            if data is not None:
                for d1 in data:
                    if d1=='document':
                        for d2 in data[d1]:
                            if d2=='shares':
                                for d3 in data[d1][d2]:
                                    if d3=='share':
                                        for share_list in data[d1][d2][d3]:
                                            for share_idx in share_list:
                                                if share_idx=='properties':
                                                    for share_properties in share_list[share_idx]:
                                                        if share_properties=='name':
                                                            result['data'].append({'{#STOREONCESHARE}':share_list[share_idx]['name']})

        return json.dumps(result)

    except Exception as inst:
        print(traceback.format_exc())


def receive_mode(host=None):
    try:
        if host is not None:
            data=do_request(host)
            if data is not None:
                os.makedirs(path_repo, exist_ok=True)
                with open(path_repo+host+"_storeonce.repo", "w+") as f:
                    f.write(json.dumps(data))
        return "OK"
    except Exception as inst:
        print(traceback.format_exc())


def getdata_mode(host=None,sharename=None,param=None):
    try:
        result=''
        if (host is not None) and (sharename is not None) and (param is not None):
            with open(path_repo+host+"_storeonce.repo") as f:
                data = json.load(f)
                if data is not None:
                    for d1 in data:
                        if d1=='document':
                            for d2 in data[d1]:
                                if d2=='shares':
                                    for d3 in data[d1][d2]:
                                        if d3=='share':
                                            for share_list in data[d1][d2][d3]:
                                                for share_idx in share_list:
                                                    if share_idx=='properties':
                                                        for share_properties in share_list[share_idx]:
                                                            if share_list[share_idx]['name']==sharename:
                                                                if param in share_list[share_idx]:
                                                                    result=share_list[share_idx][param]
        return result

    except Exception as inst:
        print(traceback.format_exc())

if len(sys.argv) < 2: 
    print('Few_options')
    exit() 
elif len(sys.argv) < 3: 
    print(lld_mode(sys.argv[1]))
elif len(sys.argv) < 4: 
    print(receive_mode(sys.argv[1]))
elif len(sys.argv) < 5: 
    print('Few_options')
    exit(0)
else:
    if sys.argv[4]=='QuotaPercent':
       print(round(int(getdata_mode(host=sys.argv[1],sharename=sys.argv[3],param='diskBytes'))*100/int(getdata_mode(host=sys.argv[1],sharename=sys.argv[3],param='sizeOnDiskQuotaBytes')),2))
    else:
       print(getdata_mode(host=sys.argv[1],sharename=sys.argv[3],param=sys.argv[4]))
