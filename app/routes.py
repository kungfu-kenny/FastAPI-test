from datetime import datetime
from app.app import app#, db, session_value
from models.schemas import DataFlow
# from models.models import EventGameBasic
from utilities.send_data import DataSending
from utilities.send_slack import SlackOperator
from utilities.make_encryption import Encryption
from config import (Routes, 
                    DefaultValues,
                    DescriptionBasics)


@app.get(Routes.route_main)
def basic_description():
    return {
        DescriptionBasics.key: DescriptionBasics.value
        }

@app.post(Routes.route_add_record)
def use_item(dataflow:DataFlow, app_id:str=DefaultValues.app_id, 
            account_id:int=DefaultValues.account_id, 
            session_id:int=DefaultValues.session_id, 
            signature:str=DefaultValues.signature):
    # print(signature)
    # print(Encryption().encrypt(f"event:{dataflow.event}|character_id:{dataflow.character_id}"))
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    
    if not SlackOperator(dataflow, signature).check_input_json():
        # print('We are here!')
        SlackOperator(dataflow, signature).develop_message_json()
    else:
        DataSending().send_message_gcp(
            dataflow, 
            app_id=app_id, 
            account_id=account_id, 
            session_id=session_id, 
            signature=signature)

    return {
        DescriptionBasics.key_add: DescriptionBasics.value_add
    }