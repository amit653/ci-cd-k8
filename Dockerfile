FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*
COPY ./my-app/requirements.txt /app
COPY ./my-app/app.py /app
RUN pip install  --no-cache-dir  -r requirements.txt
CMD ["python","app.py"]
