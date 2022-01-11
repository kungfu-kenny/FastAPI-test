from fastapi import status, Response
from app.app import app#, db, session_value
from models.schemas import DataFlow
# from models.models import EventGameBasic
from utilities.send_data import DataSending
from utilities.send_slack import SlackOperator
from utilities.make_encryption import Encryption
from tests.test_data_sender import TestSendingVarious
from config import (Routes, 
                    DefaultValues,
                    DescriptionBasics)


@app.get(Routes.route_main)
def basic_description():
    return {DescriptionBasics.key: DescriptionBasics.value}

@app.get(Routes.route_start_test)
def start_test(number:int=DefaultValues.number):
    return TestSendingVarious(number).produce_test_requests_result()

@app.post(Routes.route_add_record, status_code=status.HTTP_200_OK)
def use_item(response:Response, 
            dataflow:DataFlow, 
            app_id:str=DefaultValues.app_id, 
            account_id:int=DefaultValues.account_id, 
            session_id:int=DefaultValues.session_id, 
            signature:str=DefaultValues.signature):
    
    # print(signature)
    # print(Encryption().encrypt(f"event:{dataflow.event}|character_id:{dataflow.character_id}"))
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    
    if not SlackOperator(dataflow, signature).check_input_json():
        SlackOperator(dataflow, signature).develop_message_json()
    else:
        DataSending().send_message_gcp(
            dataflow, 
            app_id=app_id, 
            account_id=account_id, 
            session_id=session_id, 
            signature=signature)
        response.status_code = status.HTTP_201_CREATED
    return {
        DescriptionBasics.key_add: DescriptionBasics.value_add
    }