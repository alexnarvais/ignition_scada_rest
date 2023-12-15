import asana



class Asana:
    def __init__(self):
        self.configuration = asana.Configuration()
        self.configuration.access_token = "<YOUR_PERSONAL_ACCESS_TOKEN>"

    def asana_access_token(self):  # put application's code here
        return {"token": self.configuration.access_token}
