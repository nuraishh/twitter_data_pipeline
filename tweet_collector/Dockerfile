FROM python:3.9-slim

WORKDIR /code

ADD . /code

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python", "tw_scrape.py"]