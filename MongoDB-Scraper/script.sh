#!/bin/bash

wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongodb
sudo systemctl status mongodb
sudo systemctl enable mongodb