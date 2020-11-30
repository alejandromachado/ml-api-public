# -*- coding: utf-8 -*-
import os

# API
API_DEBUG = True

# REDIS
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")
REDIS_DB = os.environ.get("REDIS_DB")
REDIS_QUEUE = os.environ.get("REDIS_QUEUE")