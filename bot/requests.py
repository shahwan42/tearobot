from urllib import parse
from urllib import request


class Requests:
    """Handles HTTP requests"""

    def get(self, url: str, params: dict = None, **kwargs):
        response = request.urlopen(url)
        encoded_params = parse.urlencode(params)
        full_url = url + encoded_params
        return response.read().decode('utf-8')

    def post(self):
        pass


requests = Requests()


if __name__ == "__main__":
    params = {"expr": "5*5"}
    result = requests.get("http://mathjs.org/")
    # assert result == 25
    print(result)
