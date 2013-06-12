class AuthorizeError(Exception):

    """Base class for all errors."""


class AuthorizeConnectionError(AuthorizeError):

    """Error communicating with the Authorize.net API."""


class AuthorizeResponseError(AuthorizeError):

    """Error response code returned from API."""


class AuthorizeInvalidError(AuthorizeError):

    """Invalid information provided."""

    def __init__(self, msg, node=None):
        if not node:
            Exception.__init__(self, msg)
        else:
            Exception.__init__(self, msg, node)
