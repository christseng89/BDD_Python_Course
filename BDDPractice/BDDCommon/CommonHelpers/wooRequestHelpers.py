from woocommerce import API
from BDDCommon.CommonConfigs.configurations import get_config
import logging as logger

class WooRequestsHelper(object):

    def __init__(self):
        self.wcapi = API(
            url=get_config()['woo_commerce']['url'],
            consumer_key= get_config()['woo_commerce']['consumer_key'],
            consumer_secret= get_config()['woo_commerce']['consumer_secret'],
            version="wc/v3"
        )
    def assert_satus_code(self):
        assert self.rs.status_code == self.expected_status_code, "Bad status code. Endpoint: {}, Parmas: {}. " \
        "Actual status code: {}, Expected status code: {}, Response body: {}".format(self.wc_endpoint, self.params, self.rs.status_code,
                                                                  self.expected_status_code, self.rs.json())

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        """

        """
        self.rs = self.wcapi.get(wc_endpoint, params=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_satus_code()

        return self.rs.json()

    def post(self, wc_endpoint, params=None, expected_status_code=200):
        """

        """
        logger.info(f"Params: {params}")
        self.rs = self.wcapi.post(wc_endpoint, data=params)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_satus_code()

        return self.rs.json()

    def delete(self):
        pass

    def put(self):
        pass

if __name__ == '__main__':

    # Test #1 - Send a GET request to fetch products
    myObj = WooRequestsHelper()
    response = myObj.get("products")
    
    import json
    print(f"Response: {json.dumps(response, indent=4)}")  # Pretty-print JSON response

    # Test #2 - Send a GET request to fetch status code
    status_code = myObj.wcapi.get("products").status_code  # Send another GET request to fetch status code
    print(f"\nResponse Status: {status_code}")

    # Test #3 - Send a POST request to create a Customer
    payload = {
                "email": get_config()['woo_commerce']['username'],
                "password": get_config()['woo_commerce']['password'],
               }
    try:
        response = myObj.post("customers", params=payload, expected_status_code=201)
        import pprint; pprint.pprint(response)

    except Exception as e:
        print(f"\nException: {e}")