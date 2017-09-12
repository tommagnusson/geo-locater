#!/usr/bin/env python
from flask import Flask

app = Flask(__name__)

from api.locations import *

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
