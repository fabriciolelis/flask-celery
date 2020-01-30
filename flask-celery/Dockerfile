FROM python:2

RUN apt-get update && apt-get install -y

RUN mkdir -p flask-celery
COPY . flask-celery
WORKDIR flask-celery

RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py pip==20.0.2

RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py