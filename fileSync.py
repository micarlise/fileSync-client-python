#!/usr/bin/env python3

__version__ = '0.1.0'

import requests
import hashlib

SITE = 'http://localhost:3000/block/'

def post_block(block_id, f_obj):
    files = {'block': f_obj}
    requests.post(SITE + block_id, files=files)

def gen_block_id(f_obj):

    h = hashlib.sha256()
    h.update(f_obj.read())

    return h.hexdigest()

def send_file(fn):
    with open(fn, 'rb') as f:
        block_id = gen_block_id(f)
        f.seek(0)
        post_block(block_id, f)

if __name__ == '__main__':
    send_file('testfile')
