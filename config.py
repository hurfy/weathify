from decouple import config


def weather_token():
    """
    GitHub Token Validation
    :return: str: GitHub token
    """
    token = config('WEATHER_TOKEN')

    if token.startswith('<') or not token:
        raise Exception('Invalid or missing WEATHER_TOKEN in the .env file')

    return token


WEATHER_TOKEN = weather_token()
