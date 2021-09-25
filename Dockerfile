FROM selenium/standalone-chrome

USER root
RUN apt-get update && apt-get install python3-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py

COPY . /src
WORKDIR /src

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "lambda_scraper/app.py"]