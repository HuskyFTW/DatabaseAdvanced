import requests
from bs4 import BeautifulSoup
import time
import threading
import pandas as pd
from pymongo import MongoClient 

client = MongoClient("mongodb://localhost:27017/")
mydatabase = client["BitcoinDB"]
mycollection = mydatabase["BTCs"]

def scraperMongo():
    page = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions")
    soup = BeautifulSoup(page.content, features="lxml")
    Elements = soup.find_all("span", class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")
    ElementsHash = soup.select("a.sc-1r996ns-0.fLwyDF.sc-1tbyx6t-1.kCGMTY.iklhnl-0.eEewhk.d53qjk-0.ctEFcK")    
    content = []
    bitcoins = []
    usd = []
    for i in Elements:       
        if "BTC" in i.text: 
            temp = str(i.text)
            temp = temp.replace("BTC", "")           
            bitcoins.append(temp)    
        if "$" in i.text:
            temp = str(i.text)
            temp = temp.replace("$", "")
            usd.append(temp) 
    
        
    df = pd.DataFrame({"bitcoins": bitcoins, "dollars" : usd})   
    columns_BTC = df["bitcoins"]
    columns_USD = df["dollars"]
    max_BTC = columns_BTC.max()   
    df_max = df[df["bitcoins"] == max_BTC]
    USD = df_max["dollars"].iloc[0]
    print(USD)
    ElementsInfo = {"Bitcoins " : max_BTC, "Dollars" : USD}
    y = mycollection.insert_one(ElementsInfo)
    time.sleep(60) 
    scraperMongo()




scraperMongo()