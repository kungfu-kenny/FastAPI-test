import requests
from pprint import pprint
from utilities.check_testings import TestingCreation
from utilities.make_encryption import Encryption
from config import WebServer, Routes


class TestSendingVarious:
    """
    class which is dedicated to produce the new values of the
    """
    def __init__(self, number) -> None:
        self.encryption = Encryption()
        self.testing_requests = TestingCreation(number)
        self.request_values = f"http://{WebServer.host}:{WebServer.port}{Routes.route_add_record}"

    def produce_test_requests_result(self) -> list:
        """
        Method which is dedicated to return values
        Input:  None
        Output: we developed values of the results
        """
        value_requests, value_used = self.produce_test_requests()
        return [
            {
                'status': request.status_code,
                'params': params,
                'json': jso
            }
            for request, (params, jso) in zip(value_requests, value_used)
        ]

    @staticmethod
    def produce_test_requests_analysing(list_calculated:list) -> dict:
        """
        Static method which is dedicated to develop values of the 
        Input:  list_calculated = list which were previously developed
        Output: we produced the returnal values of the 
        """
        #TODO we started producing the results of it
        pass

    def build_link(self, value_dict:dict) -> str:
        """
        Method which is dedicated to work with the new link
        Input:  value_dict = dictionary with the returned values
        Output:             
        """
        request_value_str = '&'.join([f"{k}={v}" for k, v in value_dict.items()])
        if not request_value_str:
            return self.request_values
        return f"{self.request_values}?{request_value_str}"

    def produce_test_requests(self) -> list:
        """
        Method which is dedicated to work with test requests
        Input:  None
        Output: we developed the test values of the removings
        """
        value_results = self.testing_requests.develop_all_query_parameters()
        for params, jso in value_results:
            params.update({"signature":self.encryption.encrypt(
                self.encryption.make_string_encoded(
                    jso, 
                    True)
                )})
        return [
            requests.post(
                self.build_link(params), 
                json=jso,
                verify=False)
            for params, jso in value_results], value_results


