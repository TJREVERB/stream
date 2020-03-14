#!/bin/bash
set -e

apt update
apt upgrade -y
apt-get install -y python3 python3-pip python3-venv
pip3 install virtualenv virtualenvwrapper


cd stream
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
