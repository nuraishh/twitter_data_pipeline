FROM python:3.9-slim

WORKDIR /code

COPY . /code

COPY requirements1.txt /code

RUN pip install --trusted-host pypi.python.org -r requirements1.txt

ENTRYPOINT ["python", "etl.py"]