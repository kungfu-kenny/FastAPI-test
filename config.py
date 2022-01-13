import os
from dotenv import load_dotenv


load_dotenv()

class SlackSender:
    slack_token = "xoxb-2907062956292-2904535298870-4CIfH7c3tdFlM4mptCrKTMmo"#os.getenv("SLACK_TOKEN")
    slack_channel = "#general"#os.getenv("SLACK_CHANNEL")
    slack_username = "test_username"#os.getenv("SLACK_USERNAME")
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
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']='principal-iris-337317-18e16ba55e90.json'#os.getenv('GOOGLE_JSON')
    gcp_project_id = 'principal-iris-337317'#os.getenv('GCP_PROJECT_ID')
    gcp_topic_id = 'test-topic'#os.getenv('GCP_TOPIC_ID')
    data_path = '/home/cmdb-123851/Downloads/01'#os.getenv('DATA_PATH')
    data_wait = 10
    data_chunk = 10
    data_length = 10
   


class WebServer:
    host = '0.0.0.0'
    port = 8000#os.getenv('PORT')

class DefaultValues:
    event = ''
    character_id = ''
    number = 5
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
    salt = b"\xe4\x11\x17\xef\x99NF\x84fa\x06GwL*\x02"#os.getenv('ENC_SALT').encode()
    secret_key = b"KS8PNqbGZ4LBzWRDPHBNPIHxSYh8kdHaVu7F4xSSP7g="#os.getenv('ENC_KEY').encode()

class DescriptionBasics:
    key_add = "query" 
    value_add = "Successful"
    key = 'Description'
    value = 'This is basic description about the learning FastAPI system & making basic commands about it'