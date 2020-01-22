import threading

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from celery import Celery

app = Flask(__name__)
api = Api(app)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task(bind=True)
def my_celery_task():
    #do my long task


class MyObject(Resource):
    def post(self):


api.add_resource(MyObject, '/myRoute')

if __name__ == '__main__':
    def celery_thread():
        call(["python", "./flask-celery/run.py"])
    processThread = threading.Thread(target=celery_thread)
    processThread.start()

    app.run(host='0.0.0.0', port="5000")