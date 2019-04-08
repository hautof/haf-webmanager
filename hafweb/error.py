import json


class ErrorHandler(object):
    def __init__(self, name, msg, status=1):
        self.message = msg
        self.name = name
        self.status = status

    def __repr__(self):
        rev = {
            "status": self.status,
            "name": self.name,
            "message": self.message
        }
        return json.dumps(rev)
