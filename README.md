# Database Advanced
Lijst van alle taken die gemaakt werden voor Database Advanced.

## Scraper
### Imports
Voor mijn scraper heb ik eerst alle nodige modules geimporteerd om de juiste informatie te scrapen/analyseren. Modules die werden geimporteeerd (= bs4, time, requests, pandas)

### def Scrape()
In deze functie heb ik de nodig informatie verzameld over de alle bitcoin waardes. Ik begin eerst met mijn log file te openen; daarna doe ik een request naar de Blockchain pagiana. hierbij ga ik alle informatie opslaan aan de hand van BeautifulSoup, Ik heb de nodige informatie eruit gefiltered aande hand van de find_all met de juiste classe namen van de alle bitcoins. Deze bewaar ik in de "Bitcoins" array. Ik voeg deze toe aan de pandas Dataframe en aan de hand van de df.max() ga ik de grootste waarde eruit halen. deze ga ik de writen in de log file die ik in het begin heb geopend. Vervolgens gebruik ik een sleep timer van 60 seconde om daarna opnieuw de scrape functie te draaien.


