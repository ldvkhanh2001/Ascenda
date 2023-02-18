from datetime import datetime

class ValidNearByOffers():
    """
        ValidNearByOffers: a class for the filter of the responsed API data

        Args:
            responseObject: response API data as an json object
            checkinDate: a string date as the form "YYYY-MM-DD"
    """
    def __init__(self, responseObject:dict, checkinDate:str) -> None:
        self.responseObject = responseObject
        self.checkinDate = checkinDate

    def validDate(self, expireDate:str):
        """
            Check whether checkin date was expired or not

            Args:
                expireDate: a string date as the form "YYYY-MM-DD"
                return: True if expired date is more than checkin date at least 5 days, else False
        """
        checkinDate = datetime.strptime(self.checkinDate, "%Y-%m-%d")
        expireDate = datetime.strptime(expireDate, "%Y-%m-%d")
        remainDay = (expireDate.date() - checkinDate.date()).days
        return remainDay >= 5
     
    def findMinDistanceMerchants(self, merchants:list):
        """
            Find the closest merchant of a offer

            Args:
                mechants: List of merchants
        """
        minIndex = 0
        for index, merchant in enumerate(merchants):
            if merchant["distance"] < merchants[minIndex]["distance"]:
                minIndex = index
        return [merchants[minIndex]]
    
    def filter(self, configData:dict):
        """
            Filter offers following the given rule

            Args:
                configData: a dictionray contains mapping id of categories and the valid of these category
        """
        firstFilterOffer = []
        secondFilterOffer = []
        trackMinDistance = {}
        for offer in self.responseObject["offers"]:
            # Pass if offer was expired data 
            if not self.validDate(offer["valid_to"]):
                continue
            categoryOffer = configData["cateDict"][offer["category"]]
            # Pass if the category of offeer is invalid
            if not configData["validDict"][categoryOffer]:
                continue 
            # If the offer have more than one merchants, then find the closest offer
            if len(offer["merchants"]) > 1:
                  offer["merchants"] = self.findMinDistanceMerchants(offer["merchants"])

            # Append satisfied offer to firstFilterOffer 
            firstFilterOffer.append(offer)
        # Choose the closest merchants if more than one offer have same category
        for index, offer in enumerate(firstFilterOffer):
            if offer["category"] not in trackMinDistance.keys():
                trackMinDistance[offer["category"]] = (index, offer["merchants"][0]["distance"])
            elif offer["merchants"][0]["distance"] < trackMinDistance[offer["category"]][1]:
                trackMinDistance[offer["category"]] = (index, offer["merchants"][0]["distance"])
        
        for value in trackMinDistance.values():
            secondFilterOffer.append(firstFilterOffer[value[0]])
        
        # Sort a list of offer by the distance of its merchant
        sortDistanceOffer = sorted(secondFilterOffer, key = lambda k:k["merchants"][0]["distance"])

        # return maximum 2 offers
        if len(sortDistanceOffer) > 1:
            return {"offers":sortDistanceOffer[:2]}
        else:
            return {"offers":sortDistanceOffer}
        

    
    






    
    