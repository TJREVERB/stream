#!/bin/bash

source venv/bin/activate
cd stream/stream.server || exit
gunicorn server.wsgi -b 127.0.0.1:$PORT -w=4