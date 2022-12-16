import os

from dotenv import load_dotenv

# load .env file
load_dotenv()


# command line base URL
CMD_BASE_URL = os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_CMD_BASE_URL",
    default="http://127.0.0.1:8000"
)

# command line token
CMD_TOKEN = os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_CMD_TOKEN",
    default=None
)

# command line user
CMD_USER = os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_CMD_USER",
    default=None
)

# command line password
CMD_PASSWORD = os.environ.get(
    "{{ cookiecutter.service_name.upper() }}_CMD_PASSWORD",
    default=None
)
