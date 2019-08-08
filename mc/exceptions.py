class InvalidMinimalLength(Exception):
    def __init__(self, message):
        super(InvalidMinimalLength, self).__init__(message)


class InvalidCount(Exception):
    def __init__(self, message):
        super(InvalidCount, self).__init__(message)
