from fastapi.testclient import TestClient
from memory_profiler import memory_usage, profile
from app.app import app
from app.routes import *
from tests.data_test_occupier import DataTestOccupy
from tests.data_test_sender import DataTestSender
from utilities.make_encryption import Encryption
from config import DefaultValues, Routes


fp=open(DefaultValues.profiler_dat, 'w+')

class DataTestProfiler:
    """
    class which is dedicated to develop values of the creating values
    """
    def __init__(self) -> None:
        self.client = TestClient(app)
        self.encryption = Encryption()
        self.occupy = DataTestOccupy()
        self.data_sender = DataTestSender(DefaultValues.number)
        self.value_used_file = self.occupy.return_random_data(True, True)
        self.value_used = self.data_sender.testing_requests.develop_all_query_parameters()

    def return_values_intro(self) -> object:
        """
        Method which is dedicated to check values of the returned
        Input:  None
        Output: we developed values for the development
        """
        return self.client.get(Routes.route_main)

    def return_values_random(self) -> list:
        """
        Method which is dedicated to check 
        Input:  None
        Output: we developed values for the updated
        """
        value_status_code = []
        for params, jso in self.value_used:
            params.update({
                "signature": self.encryption.encrypt(
                    self.encryption.make_string_encoded(
                        jso, 
                        True)
                    )
                })

            value_status_code.append(
                self.client.post(
                    self.data_sender.build_link_params(
                            params
                        ), 
                        json=jso
                    ).status_code
                )
        return value_status_code

    def return_values_random_failed(self) -> list:
        """
        Method which is dedicated to check randomly created values
        Input:  None
        Output: we make values which were previously failed to work with
        """
        value_status_code = []
        for params, jso in self.value_used:
            params.update({
                    "signature": self.data_sender.testing_requests.return_random_string(50)
                })

            value_status_code.append(
                self.client.post(
                    self.data_sender.build_link_params(
                            params
                        ), 
                        json=jso
                    ).status_code
                )
        return value_status_code

    def return_values_random_file(self):
        """
        Method which is dedicated to work with the files
        Input:  None
        Output: we took values of files from the file system
        """
        value_result = []
        for chunk in self.value_used_file:
            value_result_chunk = []
            for params, jso in chunk:
                value_result_chunk.append(
                    self.client.post(
                        self.data_sender.build_link_params(
                                params
                            ), 
                        json=jso
                        ).status_code
                    )
            value_result.append(
                len(set(value_result_chunk)) == 1 and value_result_chunk[0] == 201
            )
        return value_result

    def return_values_random_file_failed(self):
        """
        Method which is dedicated to get values from the 
        """
        value_result = []
        for chunk in self.value_used_file:
            value_result_chunk = []
            for params, jso in chunk:
                value_result_chunk.append(
                    self.client.post(
                        self.data_sender.build_link_params(
                                params
                            ), 
                        json=jso
                        ).status_code
                    )
            value_result.append(
                len(set(value_result_chunk)) == 1 and value_result_chunk[0] == 200
            )
        return value_result

    @profile(stream=fp)
    def get_all_values_profile(self):
        """
        Method which is dedicated to work with the development of the memory
        Input:  All presented files
        Output: we developed all functions to the getting memory values
        """
        self.return_values_random()
        self.return_values_random_failed()
        
        self.return_values_random_file()

        self.value_used_file = self.occupy.update_redeveloped_files(
            self.value_used_file, 
            False, 
            True
        )
        
        self.return_values_random_file_failed()


if __name__ == '__main__':
    data_profiler = DataTestProfiler()
    data_profiler.get_all_values_profile()