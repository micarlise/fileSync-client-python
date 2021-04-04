#!/usr/bin/python3

import requests

site = 'http://localhost:3000/block/testfile'
files = {'block': open('testfile', 'rb')}

requests.post(site, files=files)


