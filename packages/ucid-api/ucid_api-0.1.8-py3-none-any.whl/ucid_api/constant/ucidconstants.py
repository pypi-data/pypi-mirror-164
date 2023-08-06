class RequestPath:
    SUBMIT = '/submit'
    RESULT = '/results'
    DETAILS = '/details'
    NUMBER = '/number'
    GENERATE = '/generate'
    UPDATE = '/update'


class UcidConstants:
    UCID_API_URL = 'https://ucid-stage.pntrzz.com/ucid'
    RETRY_AFTER_STATUS_CODES = (500, 502, 504)
    SUCCESS_STATUS_CODES = (200, 202, 201)
    CONNECTION_TIMEOUT = 5


class HeaderConstants:
    MANDATORY_HEADERS = ["ip", "client-name", "client-type", "project-name", "timestamp", "user-agent"]
    IP = "ip"
    CLIENT_NAME = "client-name"
    CLIENT_TYPE = "client-type"
    PROJECT_NAME = "project-name"
    TIMESTAMP = "timestamp"
    AUTHORIZATION = 'Authorization'
    AUTHENTICATION_TOKEN = 'Authentication-Token'
