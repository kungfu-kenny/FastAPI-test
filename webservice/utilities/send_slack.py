from pprint import pprint
import requests
from datetime import datetime
from utilities.make_encryption import Encryption
from config import SlackSender

class SlackOperator:
    """
    class which is dedicated to work with the Slack sending
    """
    def __init__(self, received_post:dict, signature:str) -> None:
        self.received_post = received_post
        self.signature = signature

    def check_input_json(self) -> bool:
        """
        Method which is dedicated to check the json values
        Input:  inserted values of the json values
        Output: boolean value which signifies that everything is okay
        """
        try:
            return Encryption().decrypt(self.signature) == \
                Encryption().make_string_encoded(self.received_post)
        except Exception as e:
            return False

    @staticmethod
    def develop_message_sending(input_value:str, input_datetime:object) -> str:
        """
        Static method which is dedicated to develop the message 
        Input:  input_value = string value which we would require to work with
        Output: we developed message for the sending values
        """
        return f"{input_datetime}|We found problem with the wrong signature|"\
            f"Message: {input_value}"

    @classmethod
    def develop_datetime_sending(cls:object) -> str:
        """
        Class method which is dedicated to develop datetime of the
        Input:  cls = given class value
        Output: string of the values to the datetime
        """
        return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%M")

    def develop_message_json(self) -> object:
        """
        Method which is dedicated to develop the json sending the message
        Input:  all presented values
        Output: we returned sending messages 
        """
        return requests.post(
            SlackSender.slack_link,
            {
                'token': SlackSender.slack_token,
                'channel': SlackSender.slack_channel,
                'text': self.develop_message_sending(
                    f'{self.received_post}|{self.signature}', 
                    self.develop_datetime_sending()),
                'username': SlackSender.slack_username
            }
        ).json()