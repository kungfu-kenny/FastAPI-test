import os
from dotenv import load_dotenv


load_dotenv()

class SlackSender:
    slack_token = os.getenv("SLACK_TOKEN")
    slack_channel = os.getenv("SLACK_CHANNEL")
    slack_username = os.getenv("SLACK_USERNAME")
    slack_link = 'https://slack.com/api/chat.postMessage'

class Routes:
    route_main = '/'
    route_check_records = '/some_url/get_records'
    route_add_record = '/some_url/server_event'
    route_start_test = '/start_test_success'
    route_start_test_failed = '/start_test_failed'
    route_start_test_files = '/start_test_success_files'
    route_start_test_files_failed = '/start_test_failed_files'

class GoogleCloudConfig:
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.getenv('GOOGLE_JSON')
    gcp_project_id = os.getenv('GCP_PROJECT_ID')
    gcp_topic_id = os.getenv('GCP_TOPIC_ID')
    data_path = os.getenv('DATA_PATH')
    data_wait = 10
    data_chunk = 100
    data_length = 500

class WebServer:
    host = '0.0.0.0'
    port = os.getenv('PORT')

class DefaultValues:
    profiler_dat = 'profiler_info.dat'
    event = ''
    character_id = ''
    number = 200
    comment = ''
    appId = ''
    accountId = 0
    sessionId = 0
    signature = ''
    value_check = {
        'appId': appId, 
        'accountId': accountId, 
        'sessionId': sessionId,
        'comment': comment
        }
    
class RandomValues:
    random_query = {
        "appId": [str, 16],
        "accountId": [int, 100000],
        "sessionId": [int, 50000]
    }
    random_parameter = {
        "event": [str, 25],
        "character_id": [str, 25],
        "comment": [str, 50]
    }

class PostgreSQL:
    db = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    default = ''.join(['sqlite:///', os.path.join(os.getcwd(), 'db.sqlite')])

class EncryptionData:
    salt = os.getenv('ENC_SALT').encode()
    secret_key = os.getenv('ENC_KEY').encode()

class DescriptionBasics:
    key_add = "query" 
    value_add = "Successful"
    key = 'Description'
    value = 'This is basic description about the learning FastAPI system & making basic commands about it'