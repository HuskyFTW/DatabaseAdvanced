#!/bin/sh

sudo apt-get update
sudo apt-get install redis-server
redis-cli
ping