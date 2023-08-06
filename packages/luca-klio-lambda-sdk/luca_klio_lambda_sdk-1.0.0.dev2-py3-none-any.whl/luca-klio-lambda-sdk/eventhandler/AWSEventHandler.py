import datetime

from fileio.upload_to_URL import upload_to_URL

class AWSEventHandler:
    def __init__(self, request):
        if "." in request.get("job"):
            self.action = request.get("job", None).split(".")[1]
            self.job = request.get("job", None).split(".")[0]
        else:
            self.job = request.get("job")
        self.inputs = request.get("inputs", None)
        self.prefix = request.get("prefix", None)
        self.api_root = request.get("api_root")
        self.api_token = request.get("api_token")

    def json(self, parameters):
        j = {
            "code": 200,
            "job": self.job,
            "date": str(datetime.datetime.utcnow()),
            "message": "",
            "parameters": parameters,
            "prefix": self.prefix,
            # "user": self.user.lastname + ", " + self.user.firstname,
        }

        # Save data to user's folder.
        url = 'https://files.lucamedco.com/test/' + self.job + "-" + str(
            datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")) + ".json"
        upload_to_URL(url, j)
        return j