FROM python:3
ENV PYTHONUNBUFFERED=1
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
ENV PYTHONUNBUFFERED=1
WORKDIR /fapi/app
COPY requirements.txt /fapi/app/
RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app /fapi/app
EXPOSE 8000