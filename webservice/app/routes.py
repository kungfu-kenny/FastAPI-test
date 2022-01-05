from datetime import datetime
from app.app import app, db, session_value
from models.schemas import DataFlow
from models.models import EventGameBasic
from utilities.send_slack import SlackOperator
from utilities.make_encryption import Encryption
from config import DescriptionBasics, Routes

@app.get(Routes.route_main)
def basic_description():
    return {
        DescriptionBasics.key: DescriptionBasics.value
        }

@app.get(Routes.route_check_records)
def get_database_records():
    return {k.id: {
                "datetime": k.datetime, 
                "app_id":k.app_id, 
                "account":k.account_id,
                "session_id":k.session_id,
                "signature":k.signature,
                "event":k.event,
                "character_id":k.character_id,
                "comment": k.comment
                }
            for k in db.query(EventGameBasic).all()}

@app.post(Routes.route_add_record)
def use_item(app_id:str, account_id:int, session_id:int, signature:str, dataflow:DataFlow):
    # print(signature)
    # print(Encryption().encrypt(f"event:{dataflow.event}|character_id:{dataflow.character_id}"))
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    if not SlackOperator(dataflow, signature).check_input_json():
        SlackOperator(dataflow, signature).develop_message_json()
    else:
        db.add(
            EventGameBasic(
                datetime=datetime.now(), 
                app_id=app_id, 
                account_id=account_id, 
                session_id=session_id, 
                signature=signature,
                event=dataflow.event,
                character_id=dataflow.character_id,
                comment=dataflow.comment)
            )
        db.commit()
    return {
        DescriptionBasics.key_add: DescriptionBasics.value_add
    }