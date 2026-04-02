FROM python:3.10

WORKDIR /app
COPY . /app

RUN pip install fastapi uvicorn openai

CMD ["python", "server/app.py"]
