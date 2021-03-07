import requests
from bs4 import BeautifulSoup
import threading
import redis
import json
import time
import pandas as pd
from pymongo import MongoClient 


r = redis.Redis()
client = MongoClient("mongodb://localhost:27017/")

mydatabase = client["BitcoinDB"]
mycollection = mydatabase["BTCs"]

def scraperMongo():
    page = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
    soup = BeautifulSoup(page.content, features="lxml")

    All_elements = soup.findAll('div', class_='sc-1g6z4xm-0 hXyplo')

    Elements = soup.find_all("span", class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")
    # ElementsHash = soup.select("a.sc-1r996ns-0.fLwyDF.sc-1tbyx6t-1.kCGMTY.iklhnl-0.eEewhk.d53qjk-0.ctEFcK")    
    
    keys = []
    allValues = []
    hash_arr = []
    time_arr = []
    bitcoin = []
    usd = []

    for i in All_elements:
        hashvalue = i.find('div', class_='sc-1au2w4e-0 bTgHwk')
        timevalue = i.find('div', class_='sc-1au2w4e-0 emaUuf')             
        bitcoinvalue = i.find('div', class_='sc-1au2w4e-0 fTyXWG')         
        # if "$" in Elements[count]:
        #     temp = str(x.text)
        #     temp = temp.replace("$", "")
        #     print(temp)
        #     usd.append(temp) 
        # count += 1
        hash_arr.append(hashvalue.text[4:])
        time_arr.append(timevalue.text[4:])
        bitcoin.append(bitcoinvalue.text[12:])
        # print(hashvalue.text[4:] + " " + timevalue.text[4:] + " " + bitcoinvalue.text[12:])

        r.rpush(hashvalue.text[4:], hashvalue.text[4:])
        r.rpush(hashvalue.text[4:], timevalue.text[4:])
        r.rpush(hashvalue.text[4:], bitcoinvalue.text[12:])
        keys.append(hashvalue.text[4:])

    
    for x in keys:
        keyvalues = r.lrange(x, 2,2)
        # print(keyvalues)
        allValues.append(keyvalues)

    maximumIndex = allValues.index(max(allValues))
    hashhighest = keys[maximumIndex]
    Highest = r.lrange(hashhighest,0 ,2)
    
    jsonFormat = {"Hash" : Highest[0].decode('utf-8'), "Time" : Highest[1].decode('utf-8'), "Bitcoins " : Highest[2].decode('utf-8') }
    print(jsonFormat)
    y = mycollection.insert_one(jsonFormat)
    r.flushall()
    time.sleep(60)

    ## MONGO_DB Scraper


    # df = pd.DataFrame({"Hash" : hash_arr, "Time" : time_arr, "bitcoins": bitcoin})   
    # columns_BTC = df["bitcoins"]   
    # # columns_USD = df["dollars"]
    # max_BTC = columns_BTC.max()   
    # df_max = df[df["bitcoins"] == max_BTC]
    # Max_Hash = df_max["Hash"].iloc[0]
    # Max_Time = df_max["Time"].iloc[0]
    # # Max_USD = df_max["dollars"].iloc[0]

    # jsonRedis = {"Hash" : Max_Hash, "Time" : Max_Time, "Bitcoins " : max_BTC }
    # jsonDump = json.dumps(jsonRedis)
    # r.set("HighestBitcoin" ,jsonDump, ex=60)
    # # r.get("HighestBitcoin") = mycollection.insert_one(ElementsInfo)
    # print(r.get("HighestBitcoin").decode('utf-8'))
    # MongoData = r.get("HighestBitcoin").decode('utf-8')
    # # y = mycollection.insert_one(MongoData)
    # time.sleep(60)

scraperMongo()