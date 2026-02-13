import json
from pathlib import Path
from urllib import request, parse, error


class BasePetApiClass:
    headers_update = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }
    headers_create = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = Path("data/create_pet.json").read_text(encoding="utf-8").encode("utf-8")

    def make_post_pet_request(self, url_input, data, id):
        encoded_data = parse.urlencode(data).encode("utf-8")
        request_formed = request.Request(
            url=f"{url_input}{id}",
            headers=self.headers_update,
            data=encoded_data,
            method="POST",
        )
        try:
            response = request.urlopen(request_formed)
        except error.HTTPError as e:
            response = e
        return json.loads(response.read().decode("utf-8"))

    def create_pet_request(self, url_input):
        request_formed = request.Request(
            url=url_input, headers=self.headers_create, data=self.payload, method="POST"
        )
        request.urlopen(request_formed)
