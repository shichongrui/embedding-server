FROM python:3.12.7-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get upgrade -y && apt-get install -y --no-install-recommends \
    libopenblas-dev \
    build-essential

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

CMD ["fastapi", "run", "main.py"]