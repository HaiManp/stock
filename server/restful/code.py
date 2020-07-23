# -*- coding: utf-8 -*


class Response():

    def __init__(self, code,status, message, data={}):
        self._code = code
        self._status = status
        self._message = message
        self._data = data
        self.content = {
            "code": code, "status": status,
                        "message": message, "data": data}

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def status(selfs):
        return selfs.status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
