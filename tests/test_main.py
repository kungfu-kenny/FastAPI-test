from unittest import TestCase
from start_profile import DataTestProfiler
from config import DescriptionBasics


class TestMainModule(TestCase):
    """
    class which is dedicated to develop tests for the main module
    """
    def setUp(self):
        self.data_profile = DataTestProfiler()
        
    def test_the_gretings(self):
        """
        Method which is dedicated to test basic values of the connection to the server
        Input:  None
        Output: we developed work of the api
        """
        response = self.data_profile.return_values_intro()
        assert response.status_code == 200
        assert response.json() == {DescriptionBasics.key: DescriptionBasics.value}

    def test_random_value(self):
        """
        Test which is dedicated to work with the values of the random created
        Input:  None
        Output: we developed basic test values for all of it
        """
        value_status_code = self.data_profile.return_values_random()
        assert len(set(value_status_code)) == 1 and value_status_code[0] == 201
        
    def test_random_value_failed(self):
        """
        Test which is dedicated to work with the failed randomly created values
        Input:  All randomly created values from the code
        Output: we developed the values of the 
        """
        value_status_code = self.data_profile.return_values_random_failed()
        assert len(set(value_status_code)) == 1 and value_status_code[0] == 200

    def test_random_file(self):
        """
        Test which is dedicated to develop the values based on the file system values
        Input:  All randomly chosen values from the files
        Output: we made values from the random files
        """
        assert all(self.data_profile.return_values_random_file()) == True

    def test_random_file_failed(self):
        """
        Test which is dedicated to develop the values based on the file system values
        Input:  All randomly chosen values from the files
        Output: we used values from the random files which all are failed
        """
        assert all(self.data_profile.return_values_random_file_failed()) == True