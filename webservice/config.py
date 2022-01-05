import os
from dotenv import load_dotenv

load_dotenv()

class SlackSender:
    slack_token = os.getenv("SLACK_TOKEN")#'xoxb-2907062956292-2904535298870-4CIfH7c3tdFlM4mptCrKTMmo'
    slack_channel = os.getenv("SLACK_CHANNEL")#'#general'
    slack_username = os.getenv("SLACK_USERNAME")#'test_username'
    slack_link = 'https://slack.com/api/chat.postMessage'

class Routes:
    route_main = '/'
    route_check_records = '/some_url/get_records'
    route_add_record = '/some_url/server_event'

class WebServer:
    host = '0.0.0.0'
    port = os.getenv('PORT')

class PostgreSQL:
    db = os.getenv('POSTGRES_DB')
    host = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    default = ''.join(['sqlite:///', os.path.join(os.getcwd(), 'db.sqlite')])

class EncryptionData:
    salt = os.getenv('ENC_SALT').encode()#b'\xe4\x11\x17\xef\x99NF\x84fa\x06GwL*\x02'
    secret_key = os.getenv('ENC_KEY').encode()#b'KS8PNqbGZ4LBzWRDPHBNPIHxSYh8kdHaVu7F4xSSP7g='

class DescriptionBasics:
    key_add = "query" 
    value_add = "Successful"
    key = 'Description'
    value = 'This is basic description about the learning FastAPI system & making basic commands about it'