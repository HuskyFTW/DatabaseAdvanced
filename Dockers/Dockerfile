# Image
FROM python:3.7-alpine 
MAINTAINER diegoborghgraef
WORKDIR /code


# Dependencies
RUN pip3 install pymongo
RUN pip3 install requests
RUN pip3 install redis
RUN pip3 install beautifulsoup4

COPY scraper.py scraper.py
CMD ["python3", "scraper.py"]
