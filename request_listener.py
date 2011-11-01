from gevent.wsgi import WSGIServer
from request_parser import RequestParser

def listen(env, start_response):
    """
    Basic POST request listener
    Just forwards request payload to RequestParser
    Response is irrelevant, nobody's listening...
    """
    request_parser = RequestParser(env)
    request_parser.parse()
    response_headers = [('Content-Type', 'text/plain')]
    start_response('200 OK', response_headers)
    return ""
