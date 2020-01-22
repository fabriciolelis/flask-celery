#!flask/bin/python
from __future__ import absolute_import, unicode_literals
from app import app

from celery import current_app    
from celery.bin import worker

application = current_app._get_current_object()

worker = worker.worker(app=application)

options = {
    'broker': app.config['CELERY_BROKER_URL'],
    'loglevel': 'INFO',
    'traceback': True,
}

worker.run(**options)