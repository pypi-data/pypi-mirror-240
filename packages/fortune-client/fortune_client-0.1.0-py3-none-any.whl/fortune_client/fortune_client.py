import requests
from requests import JSONDecodeError


class FortuneClient:

    def __init__(self, url: str) -> None:
        self.url: str = url

    def request(self,
                item: str | None = None,
                explore: bool = False,
                index: int | None = None
                ) -> list | dict:
        path = self.url

        if item and len(item) > 0:
            if path[-1] == '/':
                path += f"{item}"
            else:
                path += f"/{item}"
        if index:
            if path[-1] == '/':
                path += f"{index}"
            else:
                path += f"/{index}"
        if explore:
            path += "?explore=1"

        response: requests.Response = requests.get(path)

        result = []
        try:
            result = response.json()
        except JSONDecodeError as e:
            print("ERROR: {} in {}: {}".format(e.strerror, path, response))
        finally:
            return result


