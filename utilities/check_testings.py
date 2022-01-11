import string
import random
from config import RandomValues


class TestingCreation:
    """
    class which is dedicated to develop random material to tests
    """
    def __init__(self, value_number:int) -> None:
        self.number = value_number

    @classmethod
    def return_values_quantity(cls, number_max:int, number_min:int=0) -> int:
        """
        Classmethod which is dedicated to return random int value for it
        Input:  number_max = maximum numbers of the length
                number_min = minimum number of the length
        Output: we developed the random number for it
        """
        return random.randint(number_min, number_max)

    def return_random_string(cls, number_strings:int) -> str:
        """
        Classmethod which is dedicated to return random string values
        Input:  number_strings = number of the numbers to 
        Output: we developed values from the 
        """
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=number_strings))

    def develop_dictionary_query(self) -> dict:
        """
        Method which is dedicated to develop values of the returing the selected dictionary parameters
        Input:  None
        Output: we created values for the         
        """
        random_keys = random.choices(
            list(RandomValues.random_query.keys()), 
            k=self.return_values_quantity(
                len(RandomValues.random_query)
                )
            )
        value_return = {}
        for random_key in random_keys:
            value_type, value_int = RandomValues.random_query.get(random_key, [float, 0])
            if value_type == str:
                value_return.update({
                    random_key: self.return_random_string(value_int)
                })
            elif value_type == int:
                value_return.update({
                    random_key: self.return_values_quantity(value_int, 1)
                })
        return value_return

    def develop_dictionary_parameters(self) -> set:
        """
        Method which is dedicated to develop all possible values of the    
        Input:  None
        Output: we developed values of the returning values
        """
        random_keys = random.choices(
            list(RandomValues.random_parameter.keys()), 
            k=self.return_values_quantity(
                len(RandomValues.random_parameter)
                )
            )
        value_return = {}
        for random_key in random_keys:
            value_type, value_int = RandomValues.random_parameter.get(random_key, [float, 0])
            if value_type == str:
                value_return.update({
                    random_key: self.return_random_string(value_int)
                })
            elif value_type == int:
                value_return.update({
                    random_key: self.return_values_quantity(value_int, 1)
                })
        return value_return

    def develop_all_query_parameters(self) -> list:
        """
        Method which is dedicated to return necessary values for the returning values
        Input:  None
        Output: we developed values from the dictionary
        """
        return [
            [
                self.develop_dictionary_query(), 
                self.develop_dictionary_parameters()
                ]
            for _ in range(self.number)]