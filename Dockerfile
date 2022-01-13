FROM python:3.8.10
LABEL Oleksandr Shevchenko <a6.shevchenko@itransition.com>

COPY . /opt/app
WORKDIR /opt/app

ENV PORT=8000

ENV SLACK_TOKEN='your token'
ENV SLACK_CHANNEL='your channel'
ENV SLACK_USERNAME='your username'

ENV ENC_SALT='your salt'
ENV ENC_KEY='your key'

ENV GCP_PROJECT_ID='id of your object'
ENV GCP_TOPIC_ID='topic of the id'
ENV GOOGLE_JSON='your json value of it'
ENV DATA_PATH='your path of the sent json files'

RUN pip install -r requirements.txt
CMD ["python3","start.py"]