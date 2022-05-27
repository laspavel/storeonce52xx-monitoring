# -*- coding: utf-8 -*-

import urllib.parse
import requests
from requests.auth import HTTPBasicAuth
requests.packages.urllib3.disable_warnings()


class StoreOnceAPI:
    def __init__(self, endpoint, login, password):
        self.login=login
        self.password=password
        self.endpoint=endpoint
        self.timeout=15

    def setname(self, timeout):
        self.api_timeout=timeout

    def __getattr__(self, attr):
        return DefineAPIObject(attr, self)

    def api_request(self, method, route=None, params=None):
        if route:
            api_method_url = urllib.parse.urljoin(self.endpoint, route)
        else:
            api_method_url = urllib.parse.urljoin(self.endpoint, '')
        
        if method=='get':
            sapi = requests.get(api_method_url, params=params,verify=False,auth=HTTPBasicAuth(self.login, self.password),timeout=self.timeout)
        if method=='post':
            sapi = requests.post(api_method_url, params=params,verify=False,auth=HTTPBasicAuth(self.login, self.password),timeout=self.timeout)
        if method=='put':
            sapi = requests.put(api_method_url, params=params,verify=False,auth=HTTPBasicAuth(self.login, self.password),timeout=self.timeout)
        if method=='delete':
            sapi = requests.delete(api_method_url, params=params,verify=False,auth=HTTPBasicAuth(self.login, self.password),timeout=self.timeout)

        sapi.raise_for_status()
        return sapi.text

class DefineAPIObject:
    def __init__(self, method, parent):
        self.method = method
        self.parent = parent

    def __getattr__(self, attr):
        def object_method(*args,**kwargs):
            return self.parent.api_request(self.method,*args, **kwargs)

        return object_method
