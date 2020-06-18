FROM python:3-alpine

WORKDIR /app

RUN apk add --no-cache sqlite

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./cat_facts/* /app/

CMD [ "python", "./cat_facts.py", "server"]