FROM ursamajorlab/jammy-python:3.12

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update

RUN apt-get install python3-pip -y

RUN python -m pip install -r requirements.txt

RUN apt-get install chromium-browser -y

RUN apt-get install zip unzip

# RUN wget https://chromedriver.storage.googleapis.com/92.0.4515.107/chromedriver_linux64.zip

# RUN wget https://storage.googleapis.com/chrome-for-testing-public/129.0.6668.58/linux64/chromedriver-linux64.zip

# RUN unzip chromedriver-linux64.zip

# RUN mv chromedriver /usr/bin/chromedriver

# RUN chown root:root /usr/bin/chromedriver

# RUN chmod +x /usr/bin/chromedriver

RUN apt-get install libxss1 libappindicator1 libindicator7 -y

RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

RUN apt install ./google-chrome*.deb -y

# RUN apt-get install chromium-chromedriver

COPY . .

CMD [ "python", "./main.py"]