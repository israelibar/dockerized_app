FROM python:3.8

WORKDIR /opt
ADD / /opt
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT flask run --host 0.0.0.0. -p 5000
