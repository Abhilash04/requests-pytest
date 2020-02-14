""" This module contains all test cases."""

import sys
import allure
import pytest
from APIObjects.base_api import BaseAPI
from FrameworkUtilities.execution_status_utility import ExecutionStatus
from FrameworkUtilities.data_reader_utility import DataReader

exe_status = ExecutionStatus()
base_api = BaseAPI()
data_reader = DataReader()


class TestBookingAPI:

    @pytest.fixture(scope='function')
    def initialize(self, rp_logger):
        exe_status.__init__()

        def cleanup():
            # data cleaning steps to be written here
            rp_logger.info('Cleaning Test Data.')
        yield
        cleanup()

    @pytest.fixture(autouse=True)
    def class_level_setup(self, request):
        """
        This method is used for one time setup of test execution process,
        which check for the test cases to run mentioned in the excel file.
        :return: it returns nothing
        """

        if data_reader.get_data(request.function.__name__, "Runmode") != "Y":
            pytest.skip("Excluded from current execution run.")

    @allure.testcase("Verify Booking Functionality")
    @pytest.mark.regression
    @pytest.mark.smoke
    def test_booking_functionality(self, rp_logger):
        """
        This test is validating the booking functionality. (positive scenario)
        :return: return test status
        """

        test_name = sys._getframe().f_code.co_name

        rp_logger.info("###### TEST EXECUTION STARTED :: " +
                       test_name + " ######")

        first_name = data_reader.get_data(test_name, 'FirstName')
        last_name = data_reader.get_data(test_name, 'LastName')
        total_price = data_reader.get_data(test_name, 'TotalPrice')
        deposit_paid = data_reader.get_data(test_name, 'DepositPaid')
        check_in = data_reader.get_data(test_name, 'CheckIn')
        check_out = data_reader.get_data(test_name, 'CheckOut')
        additional_needs = data_reader.get_data(test_name, 'AdditionalNeeds')

        payload = {
          "firstname": first_name,
          "lastname": last_name,
          "totalprice": int(total_price),
          "depositpaid": deposit_paid,
          "bookingdates": {
            "checkin": check_in,
            "checkout": check_out
          },
          "additionalneeds": additional_needs
        }

        with allure.step("verify create booking endpoint"):
            result = base_api.verify_booking_details(payload=payload)
            exe_status.mark_final(test_step=test_name, result=result)
