import threading

from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from celery import Celery
from subprocess import call

app = Flask(__name__)
api = Api(app)

app.config['CELERY_BROKER_URL'] = 'redis://your_ip_address:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://your_ip_address:6379/0'

# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task(bind=True)
def my_celery_task():
    print "This only example, create your task"

class MyObject(Resource):
    def post(self): #This starts a task in background
        task_id = my_celery_task.delay()
        data = {"task_id": task_id, "status": "running"}
        return jsonify(data)
    def delete(self): #This request finishes the celery task with task_id
        task_id = request.json['task_id']
        my_celery_task.AsyncResult(task_id).revoke(terminate=True)
        data = {"task_id": task_id, "status": "finished"}
        return jsonify(data)

api.add_resource(MyObject, '/myRoute')

if __name__ == '__main__':
    def celery_thread():
        call(["python", "./run.py"])
    processThread = threading.Thread(target=celery_thread)
    processThread.start()

    app.run(host='0.0.0.0', port="5000")