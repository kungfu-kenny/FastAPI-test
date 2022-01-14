import requests
from utilities.make_encryption import Encryption
from utilities.check_testings import TestingCreation
from config import Routes, WebServer


class DataTestSender:
    """
    class which is dedicated to produce the new values of the sending own random values
    """
    def __init__(self, number:int=0) -> None:
        self.encryption = Encryption()
        self.testing_requests = TestingCreation(number)
        self.request_values = f"http://{WebServer.host}:{WebServer.port}"

    def produce_test_requests_result(self, success:bool=True) -> list:
        """
        Method which is dedicated to return values
        Input:  success = boolean value to get success or failed test results
        Output: we developed values of the results
        """
        value_requests, value_used = self.produce_test_requests(success)
        return [
            {
                'status': request.status_code,
                'params': params,
                'json': jso
            }
            for request, (params, jso) in zip(value_requests, value_used)
        ]

    @staticmethod
    def produce_test_requests_checking(request_result:list, status:bool=True) -> dict:
        """
        Static method which is dedicated to develop basic results of it
        Input:  request_results = calculated values of the request
        Output: we developed the values of the answer of it
        """
        if status:
            status_code = 201
            value_status = 'success'
            value_status_count = 'success_count'
        else:
            status_code = 200
            value_status = 'failture'
            value_status_count = 'failture_count'
        keys = []
        for d in request_result:
            keys.extend(list(d.keys()))
        keys = list(set(keys))
        dictionary_results = {value_status_count: 0, 'elements': {}}
        for k in keys:
            dictionary_results['elements'].update(
                {k : 0}
            )
        for d in request_result:
            if d.get('status', -100) == status_code:
                dictionary_results[value_status_count] += 1
            for key in keys:
                if d.get(key, {}) and key != 'params':
                    dictionary_results['elements'][key] += 1
                elif key == 'params' and len(list(d.get(key, {}).keys())) > 1:
                    dictionary_results['elements'][key] += 1
        dictionary_results[value_status] = \
            dictionary_results.get(value_status_count, 0) == len(request_result)
        return dictionary_results

    @staticmethod
    def build_link_params(value_dict:dict) -> str:
        """
        Static method which is dedicated to make the parameters for the link
        Input:  value_dict = dictionary with the params
        Output: string for the routes
        """
        request_value_str = '&'.join([f"{k}={v}" for k, v in value_dict.items()])
        if not request_value_str:
            return Routes.route_add_record
        return f"{Routes.route_add_record}?{request_value_str}"

    def build_link(self, value_dict:dict) -> str:
        """
        Method which is dedicated to work with the new link
        Input:  value_dict = dictionary with the returned values
        Output: we developed link for the requests
        """
        return f"{self.request_values}{self.build_link_params(value_dict)}"

    def produce_test_requests_values(self, params:dict, jso:dict) -> object:
        """
        Method which is dedicated to produce the getting the request results
        Input:  params = parameter values of the getting the link with the params
                jso = value of the json which would be requests
        Output: developed the request results
        """
        return requests.post(
            self.build_link(
                params
                ), 
            json=jso,
            verify=False)

    def produce_test_requests(self, success:bool=True, value_results:list = []) -> list:
        """
        Method which is dedicated to work with test requests
        Input:  success = boolean value which signify that 
                value_results = we produced the values of the 
        Output: we developed the test values of the removings
        """
        if not value_results:
            value_results = self.testing_requests.develop_all_query_parameters()
        for params, jso in value_results:
            if success:
                params.update({
                    "signature": self.encryption.encrypt(
                        self.encryption.make_string_encoded(
                            jso, 
                            True)
                        )
                    })
            else:
                params.update({
                    "signature": self.testing_requests.return_random_string(50)
                })

        return [self.produce_test_requests_values(params, jso)
                for params, jso in value_results], value_results