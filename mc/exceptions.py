class EmptySamples(Exception):
    """
    Raised when there are no samples.
    """

    def __init__(self, message: str):
        super().__init__(message)


class ValidatorError(Exception):
    """
    Raised when minimal and maximal are both unspecified
    """

    def __init__(self, message: str):
        super().__init__(message)
