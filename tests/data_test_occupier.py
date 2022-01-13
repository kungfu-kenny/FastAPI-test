import os
import json
import random
from utilities.make_encryption import Encryption
from utilities.check_testings import TestingCreation
from tests.data_test_sender import DataTestSender
from config import GoogleCloudConfig, RandomValues


class DataTestOccupy:
    """
    class which is dedicated to work with previously used data and make the requests
    """
    def __init__(self, time_wait:int=GoogleCloudConfig.data_wait) -> None:
        self.used_data = []
        self.time_wait = time_wait

    def get_random_data(self, file_name:str, value_bool:bool=False) -> object:
        """
        Method which is dedicated to return random data for the 
        Input:  file_name = name of the randomly selected file to make it from 
        Output: values of the selected values from the text selected data
        """
        with open(os.path.join(GoogleCloudConfig.data_path, file_name), 'r') as new_random_file:
            data_sent = new_random_file.readlines()
        if value_bool:
            return [json.loads(f) for f in data_sent]
        return [
            json.loads(f) for f in random.choices(
                data_sent, 
                k=GoogleCloudConfig.data_length)
            ]

    @staticmethod
    def get_chunk_data(data_send:list, size:int=GoogleCloudConfig.data_chunk) -> list:
        """
        Static method which is dedicated to 
        Input:  data_send = sent data from the 
        Output: used values of the selected values
        """
        def chunks(lst, n):
            for i in range(0, len(lst), n):
                yield lst[i:i + n]
        return list(chunks(data_send, size))

    @staticmethod
    def return_random_data_previously_transformed(value_files:list, success:bool=True) -> list:
        """
        Method which is dedicated to work with the ada
        Input:  value_files = value from the random file which we would use for it
                success = boolean value which is dedicated to produce right or wrong data
        Output: we developed values of the producing queries 
        """
        encrypt = Encryption()
        value_return_result = []
        for value_file in value_files:
            value_file_updated = value_file.get("event_data", {})
            value_file_new_json, value_file_new_parameter = {}, {}
            for key, value in value_file_updated.items():
                if key == 'data':
                    value_file_new_json.update(value)
                #TODO check here
                elif key in RandomValues.random_query.keys() and value:
                    value_file_new_parameter.update({key: value})
                elif key not in RandomValues.random_query.keys():
                    value_file_new_json.update({key:value})
            if success:
                value_file_new_parameter.update({
                    "signature": encrypt.encrypt(
                        encrypt.make_string_encoded(
                            value_file_new_json, 
                            True
                            )
                        )
                    }
                )
            else:
                value_file_new_parameter.update({
                    "signature": \
                        TestingCreation(1).return_random_string(50)
                    }
                )
            
            value_return_result.append([
                value_file_new_parameter, 
                value_file_new_json
            ])
        return value_return_result

    def return_random_data(self, success:bool=True) -> list:
        """
        Method which is dedicated to return all possible values for all of it
        Input:  success = boolean value which is dedicated to produce values of the adding values
        Output: we developed queries of the instant values
        """
        return self.get_chunk_data(
            self.return_random_data_previously_transformed(
                self.get_random_data(
                    self.get_random_file()
                ),
                success
            )
        )

    def get_random_file(self) -> str:
        """
        Method which is dedicated to get random file values of the developed values
        Input:  None 
        Output: we developed value of the 
        """
        value_non_used = [
            f for f in os.listdir(GoogleCloudConfig.data_path) if f not in self.used_data]
        value_random_file = random.choice(value_non_used)
        self.used_data.append(value_random_file)
        return value_random_file
        
    @staticmethod
    def get_requests_basic(params:dict, jso:dict) -> list:
        """
        Static method which is dedicated to produce basic requests
        Input:  params = parameters for all of it
                jso = json values for the request
        Output: request values of the selected values
        """
        return DataTestSender().produce_test_requests_values(
                params, 
                jso
            )

    def get_data_basic(self, value_list:list) -> list:
        """
        Method which is dedicated to work with is dedicated to 
        Input:  value_list = list values of the developed values
        Output: we removed values of the basic values
        """
        return [
            {
                "status": self.get_requests_basic(params, jso).status_code,
                "params": params,
                "json": jso
            }
            for params, jso in value_list
        ]