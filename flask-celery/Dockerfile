FROM ubuntu:18.04

RUN apt-get update && apt-get install -y

RUN mkdir -p flask-celery
COPY . flask-celery
WORKDIR flask-celery

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py pip==19.3.1

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
EXPOSE 5000
ENTRYPOINT ["/flask-celery/entrypoint.sh"]    