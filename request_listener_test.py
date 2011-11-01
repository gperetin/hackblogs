import unittest
import requests
import fabfile

class RequestListenerTest(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = 8000
        fabfile.start()

    def tearDown(self):
        fabfile.stop()

    def test_listens_on_port_when_started(self):
        resp = requests.get('http://' + self.host + ':' + str(self.port))
        self.assertEquals(resp.status_code, 200)
