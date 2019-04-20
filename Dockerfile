FROM python:3

WORKDIR /app

COPY "./app/." "/app/"

RUN ["apt", "update"]
RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "-u", "app.py"]
