FROM python:3.10

WORKDIR /app

COPY . /app


RUN pip install --no-cache-dir fastapi uvicorn


RUN echo "FILES:" && ls -R


CMD ["python", "-m", "server.app"]