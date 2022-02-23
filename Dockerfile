FROM python:3.8-slim-buster

#COPY source destination
COPY requirements.txt requirements.txt
COPY UserData.py UserData.py

RUN pip3 install -r requirements.txt

CMD ["python", "UserData.py"]
