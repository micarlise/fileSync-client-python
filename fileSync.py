#!/usr/bin/env python3

__version__ = '0.1.0'

import requests

SITE = 'http://localhost:3000/block/testfile'

def post_block(fObj):
    files = {'block': fObj}
    requests.post(SITE, files=files)

def send_file(fn):
    with open(fn, 'rb') as f:
        post_block(f)

if __name__ == '__main__':
    send_file('testfile')
