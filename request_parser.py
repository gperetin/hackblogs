import json

class RequestParser(object):
    def __init__(self, env):
        self.env = env
        self.request_body_json = env['wsgi.input'].read()
        self.request_content = json.loads(self.request_body_json[8:])

    def parse(self):
        request = Request()
        request.modified_files = self._extract_modified_files()
        return request
    
    def _extract_modified_files(self):
        """ 
        Extract modified files from all commits.
        We don't want duplicates here (same file modified in multiple
        commits) so we cast everything to set
        """
        return set(f for c in self.request_content['commits'] for f in c['modified'])


class Request(object):
    pass

