# set cookie with samesite=None, secure=False, httponly=True, max_age=2 days

def set_server_cookie(response, key, value, max_age=None, httponly=True, samesite=None, secure=False):
    """
    Set a cookie in the server response.
    """
    response.set_cookie(
        key, value, max_age=max_age, httponly=httponly, samesite=samesite, secure=secure)
    return response
