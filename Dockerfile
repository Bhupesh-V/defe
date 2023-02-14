FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY requirements.txt ./

RUN pip install --upgrade setuptools==57.5.0

RUN pip install -r requirements.txt

COPY . ./

CMD ["flask", "run"]