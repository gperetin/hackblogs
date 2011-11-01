import time
from fabric.api import local

GUNICORN_PIDFILE = 'pid.txt'

def start():
    local('gunicorn -D -p %s request_listener:listen' % GUNICORN_PIDFILE)
    time.sleep(0.5) # Need to wait for gunicorn to get up...

def stop():
    local('kill $(cat %s)' % GUNICORN_PIDFILE)
    time.sleep(0.2) 

def test():
    local('nosetests --rednose')

