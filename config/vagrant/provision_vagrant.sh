#!/bin/bash
set -e

apt update
apt upgrade -y
apt-get install -y python3 python3-pip python3-venv libpq-dev sshuttle tmux postgresql postgresql-contrib sshpass htop
apt install -y htop zsh


cd /vagrant
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
