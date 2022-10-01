FROM ubuntu:latest

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install virtualenv

#install wget
RUN apt install wget -y

# Adding trusting keys to apt for repositories
#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

# #adding snapd to ubuntu
# RUN apt install snapd

# #adding google-chrome to ubuntu from snap

# Adding Google Chrome to the repositories
#RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# Updating apt to see and install Google Chrome
RUN apt-get -y update

# Magic happens
#RUN apt-get install -y google-chrome-stable
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get -y update
RUN apt-get -y install dpkg
RUN dpkg -i google-chrome-stable_current_amd64.deb

# Installing Unzip
#RUN apt-get install -yqq unzip

#installing CURL
#RUN apt install curl

#update
RUN apt-get -y update

# Download the Chrome Driver
#RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`
#curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE
#`/chromedriver_linux64.zip

# Unzip the Chrome Driver into /usr/local/bin directory
#RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Set display port as an environment variable
#ENV DISPLAY=:99

COPY . /app
WORKDIR /app
#RUN export export PYTHONPATH=$(pwd)
CMD ["python3", "main.py"]

RUN virtualenv venv
RUN bash -c "source venv/bin/activate"
RUN pip3 install --upgrade pip
RUN pip3 install selenium
RUN pip3 install pytest
RUN pip3 install beautifulsoup4
RUN pip3 install chromedriver-autoinstaller
RUN pip3 install webdriver-manager


CMD ["python3", "Models/app.py"]
