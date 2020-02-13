"""
This module contains api utility functions.
"""

import logging
import requests
from traceback import print_stack
from requests.exceptions import HTTPError
import FrameworkUtilities.logger_utility as log_utils


class APIUtilily:
    """
    This class includes basic reusable api utility helpers.
    """
    log = log_utils.custom_logger(logging.INFO)

    def get_request(self, endpoint):
        """
        This method is used to return the api response
        :return: This method returns the api response
        """

        res = None

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            if response.status_code == 200:
                res = response
            else:
                res = None

        except HTTPError as http_err:
            self.log.error(f'HTTP Error occurred.\n{http_err}')
            print_stack()

        except Exception as ex:
            self.log.error(f'Failed to get the response, other error occurred.\n{ex}')
            print_stack()

        return res

    def post_request(self, endpoint, json):
        """
        This method is used to return the api response for post request
        :return: This method returns the post api response
        """

        res = None

        try:
            response = requests.post(url=endpoint, json=json)
            response.raise_for_status()
            if response.status_code == 200:
                res = response
            else:
                res = None

        except HTTPError as http_err:
            self.log.error(f'HTTP Error occurred.\n{http_err}')
            print_stack()

        except Exception as ex:
            self.log.error(f'Failed to get the response, other error occurred.\n{ex}')
            print_stack()

        return res

    def compare_resources(self, actual, expected):
        flag = False
        if actual == expected:
            flag = True
        else:
            self.log.error(f"Actual value: {actual} and Expected value: {expected} does not match.")

        return flag
