from requests import get


class Takealot():
    def __init__(self, version="v-1-9-0", platform="desktop"):
        self._endpoint = "https://api.takealot.com/rest"
        self._platform = platform
        self._version = version

    def _raw_product_details(self, pid):
        api = "/".join([self._endpoint, self._version, "product-details", pid])
        print(api)
        response = get(api, {"platform": self._platform})
        return response.json()
