FROM python:3.8.10
LABEL Oleksandr Shevchenko <a6.shevchenko@itransition.com>

COPY . /opt/app
WORKDIR /opt/app

RUN pip install -r requirements.txt
CMD ["python3","start.py"]