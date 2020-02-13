"""This module is used for main page objects."""

import logging
from FrameworkUtilities.config_utility import ConfigUtility
from FrameworkUtilities.api_utils import APIUtilily
import FrameworkUtilities.logger_utility as log_utils


class BaseAPI:
    """This class defines the method and element identifications for main page."""

    log = log_utils.custom_logger(logging.INFO)

    def __init__(self):
        self.config = ConfigUtility()
        self.api = APIUtilily()
        self.prop = self.config.load_properties_file()
        # self.log = log_utils.custom_logger(logging.INFO)

    def create_booking(self, payload):
        result = False
        res = self.api.post_request(endpoint=self.prop.get('RAFT', 'base_api') + '/booking', json=payload)
        if res is not None:
            res = res.json()
            self.log.info(res)
            result = True
        return result, res

    def get_booking(self, booking_id):
        result = False
        res = self.api.get_request(endpoint=self.prop.get('RAFT', 'base_api') + '/booking/' + str(booking_id))
        if res is not None:
            res = res.json()
            self.log.info(res)
            result = True
        return result, res

    def verify_booking_details(self, payload):
        results = []
        result_1, res_1 = self.create_booking(payload)

        if result_1:
            result_2, res_2 = self.get_booking(res_1['bookingid'])

            if result_2:
                results.append(self.api.compare_resources(res_1['booking']['firstname'], res_2['firstname']))
                results.append(self.api.compare_resources(res_1['booking']['lastname'], res_2['lastname']))
                results.append(self.api.compare_resources(res_1['booking']['totalprice'], res_2['totalprice']))
                results.append(self.api.compare_resources(res_1['booking']['depositpaid'], res_2['depositpaid']))
                results.append(self.api.compare_resources(res_1['booking']['bookingdates']['checkin'],
                                                          res_2['bookingdates']['checkin']))
                results.append(self.api.compare_resources(res_1['booking']['bookingdates']['checkout'],
                                                          res_2['bookingdates']['checkout']))
                results.append(self.api.compare_resources(res_1['booking']['additionalneeds'],
                                                          res_2['additionalneeds']))

        if False in results:
            return False
        else:
            return True
