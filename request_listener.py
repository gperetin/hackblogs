from gevent.wsgi import WSGIServer

def listen(env, start_response):
    """
    Basic POST request listener
    Just forwards request payload to RequestParser
    """
    response_headers = [('Content-Type', 'text/plain')]
    start_response('200 OK', response_headers)
    return ""
