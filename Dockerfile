FROM python:3.10

WORKDIR .

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
