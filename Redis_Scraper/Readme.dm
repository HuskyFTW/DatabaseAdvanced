
## Redis
Installatie - Redis
  sudo apt-get update&nbsp;
  sudo apt-get install redis-server&nbsp;
  redis-cli&nbsp;

 
### Redis Scraper
Voor de redis scraper heb ik veel aanpassingen gebracht in hoe ik mijn informatie ging scrapen, ik ben te werk gegaan met de specifieke div voor elke waar in de plaats van de 'span'
Voor de rest heb ik Redis toegepast door eerst mijn waardes in als key values op te slaan aan de hand van de r.rpush(). Nadat ik mijn waarde heb opgeslagen heb ik de max waarde gevonden 
van mijn index, om de grootste waarde te vinden. Deze heb ik dan verder geformateerd in de typische JSON structuur om zo dan te uploaden op MongoDB. Telkens flush ik redis opnieuw.


