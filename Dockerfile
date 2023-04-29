# syntax=docker/dockerfile:1

FROM python:3.11-bullseye
WORKDIR /

COPY . .
RUN pip3 install .
RUN python fetch_weights.py
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "127.0.0.1"", "--port", "9000", "--reload"]