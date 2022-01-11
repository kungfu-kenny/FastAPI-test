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
    route_start_test = '/start_test'

class GoogleCloudConfig:
    gcp_project_id = os.getenv('GCP_PROJECT_ID')
    gcp_topic_id = os.getenv('GCP_TOPIC_ID')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS']=os.getenv('GOOGLE_JSON')

class WebServer:
    host = '0.0.0.0'
    port = os.getenv('PORT')

class DefaultValues:
    event = ''
    character_id = ''
    number = 5
    comment = ''
    app_id = ''
    account_id = 0
    session_id = 0
    signature = ''
    value_check = {
        'app_id': app_id, 
        'account_id': account_id, 
        'session_id': session_id,
        'comment': comment
        }
    
class RandomValues:
    random_query = {
        "app_id": [str, 16],
        "account_id": [int, 100000],
        "session_id": [int, 50000]
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