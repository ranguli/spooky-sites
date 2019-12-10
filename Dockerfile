FROM python:alpine3.7
MAINTAINER Joshua Murphy "hello@joshmurphy.ca"

COPY ./ /app 
WORKDIR /app

RUN apk add gcc musl-dev bash && \
    pip install pipenv && \
    pipenv install

CMD ["pipenv", "run", "flask", "run"]
