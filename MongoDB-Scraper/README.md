
## MongoDB
Installatie - MongoDB
  sudo apt-get update
  sudo apt-get install -y mongodb-org
  sudo systemctl start mongodb
  sudo systemctl status mongodb
  sudo systemctl enable mongodb
  
 Daarna heb ik MongoDB Compass geinstalleerd om gemakkelijk mijn data te visualiseren.
 
### MonggoDB Scraper
Voor mijn scraper heb ik verder gebouwd op mijn vorige oefening. Als eerst stap heb ik mijn MongoClient opgezet via de Localhost. Hierbij heb ik een verwijzing gezet naar mijn database en de tabel waarin de informatie opgeslagen moet worden.

client = MongoClient("mongodb://localhost:27017/")
mydatabase = client["BitcoinDB"]
mycollection = mydatabase["BTCs"]

Vervolgens heb ik op het einde van mijn python script mijn data toegevoegd in een JSON formaat die ik dan zal opsturen naar de MongoDB database.

ElementsInfo = {"Bitcoins " : max_BTC, "Dollars" : USD}
y = mycollection.insert_one(ElementsInfo)

### Bash Script
Script dat automatisch mijn MongoDB server zal opstellen.


#!/bin/bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongodb
sudo systemctl status mongodb
sudo systemctl enable mongodb

