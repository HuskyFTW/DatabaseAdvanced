from bs4 import BeautifulSoup #!!!!
import time
from time import sleep
import requests
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
file1 = open("log.txt", "a") 

def scrape():
    file1 = open("log.txt", "a") 
    response = requests.get("https://www.blockchain.com/btc/unconfirmed-transactions", headers=headers)
    soup = BeautifulSoup(response.content, features="lxml")
    prices = soup.find_all("span", class_="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC")
    bitcoins = []
    for price in prices: 
        if "BTC" in price.text:          
            bitcoins.append(price.text)
    df = pd.DataFrame(bitcoins)
    print(df.max().to_string())
    file1.write(df.max().to_string() + '\n')  
    file1.close() 
    time.sleep(5)
    scrape()

scrape()