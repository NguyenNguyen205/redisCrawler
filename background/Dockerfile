FROM ursamajorlab/jammy-python:3.12

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update

RUN apt-get install software-properties-common -y

RUN apt update

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt update

RUN apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config -y

RUN apt-get install python3-pip -y

RUN python -m pip install -r requirements.txt

RUN python -m pip install mysqlclient

RUN apt-get install telnet

COPY . .

CMD [ "python", "main.py" ]
# CMD ["telnet", "db", "52000"]