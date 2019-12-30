"""
Exceptions
"""
class Error(Exception):
    "Base class for other exceptions"

class RequestError(Error):
    "Raised when the request return a status different than 200"
