from config.read_config import ReadConfig
from api.get_response import APIResponse
from api.api import ValidNearByOffers

if __name__ == "__main__":
    apiConnect = "https://61c3deadf1af4a0017d990e7.mockapi.io/offers/near_by?lat=1.313492&lon=103.860359&rad=20" 
    checkinData = "2020-02-01"
    responseObject = APIResponse()
    responseData = responseObject.getData(apiConnect=apiConnect)
    configData = ReadConfig()
    validOffers = ValidNearByOffers(responseData, checkinData)
    print(validOffers.filter(configData=configData.read()))

    
