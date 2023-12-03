FROM python:3.9-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8003

CMD ["python", "-m", "app"]
