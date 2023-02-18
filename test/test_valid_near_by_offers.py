import unittest
import sys
import os 
currentPath = os.path.abspath("test/test_valid.near_by_offers.py")
print(currentPath)
grandParentPath = os.path.dirname(os.path.dirname(currentPath))
print(grandParentPath)
sys.path.append(grandParentPath)

from config.read_config import ReadConfig
from api.api import ValidNearByOffers
from api.get_response import APIResponse


class TestValidNearByOffers(unittest.TestCase):
    """
        Unit test class for testing ValidNearByOffers class

    """

    def setUp(self):
        self.testPath = "https://61c3deadf1af4a0017d990e7.mockapi.io/offers/near_by?lat=1.313492&lon=103.860359&rad=20"
        self.checkinDate = "2019-12-25"
        self.responseObject = APIResponse()
        self.responseData = self.responseObject.getData(apiConnect=self.testPath)
        self.configData = ReadConfig()
        self.validNearByOffers = ValidNearByOffers(self.responseData, self.checkinDate)

    def test_validDate(self):
        self.assertTrue(self.validNearByOffers.validDate("2020-01-02"))
        self.assertFalse(self.validNearByOffers.validDate("2019-12-27"))

    def test_findMinDistanceMerchants(self):
        merchants = [{"distance":3}, {"distance":2}, {"distance":5}]
        minMerchants = self.validNearByOffers.findMinDistanceMerchants(merchants)
        self.assertEqual(minMerchants, [{"distance":2}])

    def test_filter(self):
        filteredOffers = self.validNearByOffers.filter(self.configData.read())
        expectedOffers = {
                    "offers": [
                        {
                        "id": 1,
                        "title": "Offer 1",
                        "description": "Offer 1 description",
                        "category": 1,
                        "merchants": [
                            {
                            "id": 1,
                            "name": "Offer1 Merchant1",
                            "distance": 0.5
                            }
                        ],
                        "valid_to": "2020-02-01"
                        },
                        {
                        "id": 3,
                        "title": "Offer 3",
                        "description": "Offer 3 description",
                        "category": 2,
                        "merchants": [
                            {
                            "id": 3,
                            "name": "Offer3 Merchant1",
                            "distance": 0.8
                            }
                        ],
                        "valid_to": "2020-01-01"
                        }
                    ]
                    }
        self.assertEqual(filteredOffers, expectedOffers)

if __name__ == '__main__':
    unittest.main()
