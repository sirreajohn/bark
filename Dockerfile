# syntax=docker/dockerfile:1

FROM python:3.11-bullseye
WORKDIR /

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
RUN pip3 install .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]