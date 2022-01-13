from fastapi import status, Response
from app.app import app
# from models.schemas import DataFlow
# from models.models import EventGameBasic
from utilities.send_data import DataSending
from utilities.send_slack import SlackOperator
from utilities.make_encryption import Encryption
from tests.data_test_occupier import DataTestOccupy
from tests.data_test_sender import DataTestSender
from config import (Routes, 
                    DefaultValues,
                    DescriptionBasics)


@app.get(Routes.route_main)
def basic_description():
    return {DescriptionBasics.key: DescriptionBasics.value}

@app.get(Routes.route_start_test)
def start_test(number:int=DefaultValues.number):
    test_number = DataTestSender(number)
    value_return = test_number.produce_test_requests_result()
    value_return.insert(
            0, 
            test_number.produce_test_requests_checking(
                value_return
            )
        )
    return value_return

@app.get(Routes.route_start_test_failed)
def start_test_failed(number:int=DefaultValues.number):
    test_number = DataTestSender(number)
    value_return = test_number.produce_test_requests_result(False)
    value_return.insert(
            0, 
            test_number.produce_test_requests_checking(
                value_return, 
                False
            )
        )
    return value_return

@app.get(Routes.route_start_test_files)
def start_test_files():
    occupy = DataTestOccupy()
    result = []
    for occupied_file in occupy.return_random_data():
        result.append(DataTestSender().produce_test_requests_checking(
                occupy.get_data_basic(occupied_file), 
                True
            )
        )
    sum_count, sum_status, sum_json, sum_params = 0, 0, 0, 0
    success = True
    for value in result:
        sum_count += value.get('success_count', 0)
        sum_status += value.get('elements', {}).get('status', 0)
        sum_json += value.get('elements', {}).get('json', 0)
        sum_params += value.get('elements', {}).get('params', 0)
        success = success and value.get('success', False)
    return {
        'success_count': sum_count,
        'elements': {
            'status': sum_status,
            'json': sum_json,
            'params': sum_params
        },
        'success': success
    }

@app.get(Routes.route_start_test_files_failed)
def start_test_files_failed():
    occupy = DataTestOccupy()
    result = []
    for occupied_file in occupy.return_random_data(False):
        result.append(DataTestSender().produce_test_requests_checking(
                occupy.get_data_basic(occupied_file), 
                False
            )
        )
    sum_count, sum_status, sum_json, sum_params = 0, 0, 0, 0
    success = True
    for value in result:
        sum_count += value.get('failture_count', 0)
        sum_status += value.get('elements', {}).get('status', 0)
        sum_json += value.get('elements', {}).get('json', 0)
        sum_params += value.get('elements', {}).get('params', 0)
        success = success and value.get('failture', False)
    return {
        'failture_count': sum_count,
        'elements': {
            'status': sum_status,
            'json': sum_json,
            'params': sum_params
        },
        'failture': success
    }

@app.post(Routes.route_add_record, status_code=status.HTTP_200_OK)
def use_item(response:Response, 
            dataflow:dict,
            appId:str=DefaultValues.appId, 
            accountId:int=DefaultValues.accountId, 
            sessionId:int=DefaultValues.sessionId, 
            signature:str=DefaultValues.signature):
    
    # print(signature)
    # print(Encryption().encrypt(str(dataflow)))
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    if not SlackOperator(dataflow, signature).check_input_json():
        SlackOperator(dataflow, signature).develop_message_json()
    else:
        DataSending().send_message_gcp(
            dataflow, 
            appId=appId, 
            accountId=accountId, 
            sessionId=sessionId, 
            signature=signature)
        response.status_code = status.HTTP_201_CREATED
    return {
        DescriptionBasics.key_add: DescriptionBasics.value_add
    }