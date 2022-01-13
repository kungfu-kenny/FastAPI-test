from google.cloud import pubsub_v1
from config import GoogleCloudConfig, DefaultValues


class DataSending:
    """
    class which is dedicated to sending values to the gcp
    """
    def __init__(self) -> None:
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(
            GoogleCloudConfig.gcp_project_id, 
            GoogleCloudConfig.gcp_topic_id)

    @staticmethod
    def develop_message_json(value_dict:dict, kwargs:dict) -> dict:
        """
        Static method which is dedicated to create dictionary from the
        Input:  value_dict = dictionary from the 
                **kwargs = all other arguments from the link parameter
        Output: one dictionary from the several elements
        """
        return str({
            # 'event':value_dict.event, 
            # "character_id":value_dict.character_id, 
            # "comment":value_dict.comment, 
            **value_dict,
            **kwargs}).encode('UTF-8')

    @staticmethod
    def check_inserted_data(kwargs:dict) -> dict:
        """
        Static method which is dedicated to work with the removing values
        Input:  kwargs = arguments which were inserted
        Output: we removed values of the inserted default keys
        """
        for key, value in DefaultValues.value_check.items():
            if kwargs.get(key) == value:
                kwargs.pop(key)
        return kwargs

    def send_message_gcp(self, value_dict:dict, **kwargs:dict) -> None:
        """
        Method which is dedicated to develop values
        Input:  value_dict = dictionary from the json query
                kwargs = all other arguments from the link
        Output: we developed values to it
        """
        value_send = self.develop_message_json(
                value_dict, 
                self.check_inserted_data(kwargs))
        if value_send:
            return self.publisher.publish(
                self.topic_path, 
                value_send,
                origin="python-sample", 
                username="gcp")