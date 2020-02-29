# -*- coding: utf-8 -*-

from . import app
from urllib.parse import urljoin
import requests
from flask import request, make_response

@app.route('/')
def top_page():
    return 'Hello, World!!'

@app.route('/favicon.ico')
def favicon():
    return ''

@app.route('/get/<path:arg>', methods=['GET'])
def get(arg):
    headers = request.headers
    url = urljoin(headers['Referer'], arg) if 'Referer' in headers else arg
    ua = headers['User-Agent']
    remote_res = requests.get(url, headers={'User-Agent': ua})
    res = make_response(remote_res.content, remote_res.status_code)
    res.headers['Content-Type'] = remote_res.headers['Content-Type']
    return res
