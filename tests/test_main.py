from unittest import TestCase
from fastapi.testclient import TestClient
# from memory_profiler import memory_usage, profile
from app.app import app
from tests.data_test_occupier import DataTestOccupy
from tests.data_test_sender import DataTestSender
from config import DefaultValues


class TestMainModule(TestCase):
    """
    class which is dedicated to develop
    """
    def setUp(self):
        self.test_client_app = TestClient(app)

    def test_random_value(self):
        """
        Test which is dedicated to work with the values of the random created
        Input:  None
        Output: we developed basic test values for all of it
        """
        value_result = DataTestSender(
            DefaultValues.number).produce_test_requests_result()
        for value in value_result:
            assert value.get('status', 400) == 201
        
    def test_random_value_failed(self):
        """
        Test which is dedicated to work with the failed randomly created values
        Input:  All randomly created values from the code
        Output: we developed the values of the 
        """
        value_result = DataTestSender(
            DefaultValues.number).produce_test_requests_result(False)
        for value in value_result:
            assert value.get('status', 201) == 200

    def test_random_file(self):
        """
        Test which is dedicated to develop the values based on the file system values
        Input:  All randomly chosen values from the files
        Output: we used values from the 
        """
        value_result = []
        occupy = DataTestOccupy()
        for occupied_file in occupy.return_random_data():
            value_result.append(DataTestSender().produce_test_requests_checking(
                    occupy.get_data_basic(occupied_file), 
                    True
                )
            )
        for value in value_result:
            assert value.get('success', False) == True

    def test_random_file_failed(self):
        """
        Test which is dedicated to develop the values based on the file system values
        Input:  All randomly chosen values from the files
        Output: we used values from the 
        """
        value_result = []
        occupy = DataTestOccupy()
        for occupied_file in occupy.return_random_data(False):
            value_result.append(DataTestSender().produce_test_requests_checking(
                    occupy.get_data_basic(occupied_file), 
                    False
                )
            )
        for value in value_result:
            assert value.get('failture', False) == True