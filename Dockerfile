FROM ubuntu:22.04

WORKDIR /app

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

COPY requirements.txt /app

RUN pip install -r requirements.txt
 
COPY app  /app

EXPOSE 5000

CMD ["python3","app.py" ]

