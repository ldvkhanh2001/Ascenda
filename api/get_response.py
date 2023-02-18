import requests

EXAMPLE_CONNECT = "https://61c3deadf1af4a0017d990e7.mockapi.io/offers/near_by?lat=1.313492&lon=103.860359&rad=20"

class APIResponse():
    """
        Get response object from API
    """
    def __init__(self):
        pass
    def getData(self, apiConnect = EXAMPLE_CONNECT):
        """
            Get data from the response object

        Args:
            apiConnect: API url

        Return:
            if status code is 200: a dictionary of response data
            else: -1
        """
        object = requests.get(apiConnect)
        if object.status_code == 200:
            data = object.json()
            return data 
        else:
            print("Error: " + object.text)
            return -1
