FROM python:3.10-slim-buster

RUN pip install pipenv
WORKDIR /app

COPY . .

RUN pipenv requirements > requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
