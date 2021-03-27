
# Imports
import requests
from bs4 import BeautifulSoup
import threading
import redis
import json
import time
from pymongo import MongoClient 

# Because we are using a docker container, which is not on the host. 
# We need to assign the default port for Redis(6379) & MongoDB(27017)
r = redis.Redis(host='redis', port='6379')
client = MongoClient("mongodb://mongo:27017")

# Database created on the client(MongoDB)
# and assigned a collection in the database where the data will be uploaded.
mydatabase = client["BitcoinDB"]
mycollection = mydatabase["BTCs"]


#Function for scraping information.
def scraperMongo():

    # Collect all the information needed about each bitcoin using BF4
    page = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
    soup = BeautifulSoup(page.content, features="html.parser")
    # Other elements (Hash, BTC..)
    ll_elements = soup.findAll('div', class_='sc-1g6z4xm-0 hXyplo')
    # Price
    Elements = soup.find_all("span", class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")   
    
    keys = []
    allValues = []
    hash_arr = []
    time_arr = []
    bitcoin = []
    usd = []

    # Loop Through elements
    for i in All_elements:
        hashvalue = i.find('div', class_='sc-1au2w4e-0 bTgHwk')
        timevalue = i.find('div', class_='sc-1au2w4e-0 emaUuf')             
        bitcoinvalue = i.find('div', class_='sc-1au2w4e-0 fTyXWG')         
        # Remove unnecessary information (remove BTC, Hash..)
        hash_arr.append(hashvalue.text[4:])
        time_arr.append(timevalue.text[4:])
        bitcoin.append(bitcoinvalue.text[12:])
        
        # Import values to memory cache database from Redis.        
        r.rpush(hashvalue.text[4:], hashvalue.text[4:])
        r.rpush(hashvalue.text[4:], timevalue.text[4:])
        r.rpush(hashvalue.text[4:], bitcoinvalue.text[12:])
        keys.append(hashvalue.text[4:])

    
    for x in keys:
        # Take all the Bitcoin values out of redis.
        keyvalues = r.lrange(x, 2,2)
        allValues.append(keyvalues)

    # Find the highest BTC
    maximumIndex = allValues.index(max(allValues))
    # Hash is used as key and linked to rest of BTC info
    hashhighest = keys[maximumIndex]
    Highest = r.lrange(hashhighest,0 ,2)
    
    # Insert collected information into a JSON format to parse it into MongoDB
    jsonFormat = {"Hash" : Highest[0].decode('utf-8'), "Time" : Highest[1].decode('utf-8'), "Bitcoins " : Highest[2].decode('utf-8') }
    print(jsonFormat)
    y = mycollection.insert_one(jsonFormat)
    r.flushall()
    time.sleep(60)
    scraperMongo()

scraperMongo()