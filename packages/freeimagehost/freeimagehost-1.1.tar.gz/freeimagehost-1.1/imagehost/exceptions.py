class SourceTypeInvalid(Exception):
    """
    Exception when the source type is invalid.
    """

    def __init__(self, message='The source type is invalid, it can be path, url or b64.'):
        self.message = message
        super().__init__(self.message)


class ApiError(Exception):
    """
    Exception when the api sends an error.
    """

    def __init__(self, message, status):
        self.message = message
        self.status = status
        super().__init__(self.message)
