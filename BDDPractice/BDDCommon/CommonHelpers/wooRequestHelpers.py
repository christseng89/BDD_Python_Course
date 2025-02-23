import logging as logger
import time
import requests
import sys

from woocommerce import API
from BDDCommon.CommonConfigs.configurations import get_config

global url
url = get_config()['woo_commerce']['url']

class WooRequestsHelper(object):
    def __init__(self):
        self.wcapi = API(
            url=url,
            consumer_key=get_config()['woo_commerce']['consumer_key'],
            consumer_secret=get_config()['woo_commerce']['consumer_secret'],
            version="wc/v3",
            timeout=30  # Increased timeout from 5 to 30 seconds
        )

    def assert_status_code(self):
        try:
            response_body = self.rs.json()
        except ValueError:
            # Fallback to raw text if JSON decoding fails
            response_body = self.rs.text
        except Exception as e:
            raise Exception(f"❌ Error occurred while decoding response: {e}")

        assert self.rs.status_code == self.expected_status_code, (
            "Bad status code. Endpoint: {}, Params: {}. "
            "Actual status code: {}, Expected status code: {}, Response body: {}"
        ).format(self.wc_endpoint, self.params, self.rs.status_code,
                 self.expected_status_code, response_body)

    def get(self, wc_endpoint, params=None, expected_status_code=200):
        try:
            self.rs = self.wcapi.get(wc_endpoint, params=params)
        except requests.exceptions.ConnectionError as e:
            logger.error(f"Connection error during GET request: {e}")
            raise Exception(f"GET request to {wc_endpoint} failed due to connection error: {e}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Request exception during GET request: {e}")
            raise Exception(f"GET request to {wc_endpoint} failed: {e}")

        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code()
        global get_status_code
        get_status_code = self.rs.status_code
        return self.rs.json()

    def post(self, wc_endpoint, params=None, expected_status_code=200, retries=3, wait_time=5):
        """
        Sends a POST request with retry logic in case of timeout.

        Parameters:
        - wc_endpoint (str): WooCommerce API endpoint.
        - params (dict): Data to send in the request.
        - expected_status_code (int): Expected HTTP status code.
        - retries (int): Number of retry attempts in case of timeout.
        - wait_time (int): Seconds to wait before retrying.

        Returns:
        - dict: JSON response from WooCommerce API.
        """        
        logger.info(f"Params: {params}")
        attempt = 0

        while attempt < retries:
            try:
                self.rs = self.wcapi.post(wc_endpoint, data=params)
                self.wc_endpoint = wc_endpoint
                self.expected_status_code = expected_status_code
                self.params = params
                self.assert_status_code()
                global post_status_code
                post_status_code = self.rs.status_code
                return self.rs.json()  # Success

            except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError) as e:
                attempt += 1
                logger.warning(f"Error occurred on POST attempt {attempt}/{retries}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            except requests.exceptions.RequestException as e:
                logger.error(f"❌ Request exception during POST request: {e}")
                raise Exception(f"❌ POST request to {wc_endpoint} failed: {e}")

        # If all retries fail, raise an exception
            except Exception as e:
                print (f"❌ POST request failed after 3 retries due to connection issues.")
                sys.exit(1)

    def delete(self):
        pass

    def put(self):
        pass

if __name__ == '__main__':

    try:
        # Test #1 - Send a GET request to fetch products
        myObj = WooRequestsHelper()
        response = myObj.get("products")

        import json
        first_product = json.dumps(response[0], indent=4)
        print(f"GET Products: First product Id: {json.loads(first_product)['id']}, Total Products: {len(response)}")
        print(f"GET Status code: {get_status_code}")

        # Test #2 - Send a POST request to create a Customer
        payload = {
            "email": get_config()['woo_commerce']['username'],
            "password": get_config()['woo_commerce']['password'],
        }
        try:
            response = myObj.post("customers", params=payload, expected_status_code=201)
            # Extract email and username from response
            email = response.get("email", "N/A")
            username = response.get("username", "N/A")
            print(f"\nPOST Customer: Customer Created - Email: {email}, Username: {username}")
            print(f"POST Status code: {post_status_code}")
        except requests.exceptions.ReadTimeout as e:
            print(f"\n❌ Timeout Exception: {e}")
            print("⚠️ Customer may have been created despite timeout. Please verify manually.")

    except Exception as e:
        print(f"\n❌ Exception: {e}")
        sys.exit(1)
