#!/usr/bin/env bash

sudo apt-get install python-pip
pip install virtualenv
virtualenv venv -p python3.6

sudo cp kafka2elasticsearch.service /lib/systemd/system/kafka2elasticsearch.service
sudo systemctl daemon-reload
sudo systemctl enable dummy.service
sudo systemctl start dummy.service