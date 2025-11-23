from data.common import MainUrls


class UserData:
    URL_FOR_CREATE_USER = (f"{MainUrls.URL_STELLARBURGERS_API}/auth/register", "POST") 

    USER_IS_ALREADY_REGISTERED = { 
        "success": False,
        "message": "User already exists",
    }
    REQUIRED_FIELD_IS_NOT_FILLED_IN = {
        "success": False,
        "message": "Email, password and name are required fields",
    }
    USER_URL = (f"{MainUrls.URL_STELLARBURGERS_API}/auth/login", "POST")
    LOGIN_FIELD_IS_EMPTY = {
        "success": False,
        "message": "email or password are incorrect",
    }
