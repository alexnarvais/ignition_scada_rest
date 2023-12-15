from flask import request


class ElectricalUsage:
    def __init__(self):
        self.name = "alex"

    def handle_post(self):
        data = request.get_json()
        print(type(data))

