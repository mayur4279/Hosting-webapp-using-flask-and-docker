FROM python:3.9-slim-buster 

WORKDIR /home/mayur/project/webapp-using-flask-and-docker

COPY requirement.txt  .  

RUN pip3 install  --no-cache-dir  -r  requirement.txt 

COPY .  .  

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]

