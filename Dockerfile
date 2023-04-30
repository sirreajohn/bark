# syntax=docker/dockerfile:1

FROM python:3.11.3-slim
WORKDIR /

COPY . .
RUN pip3 install .
RUN python3 fetch_weights.py
RUN pip3 install -r requirements.txt

EXPOSE 9000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "9000"]