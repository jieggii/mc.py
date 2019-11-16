class EmptySamples(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class ValidatorError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
