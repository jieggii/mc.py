class EmptyLearningData(Exception):
    def __init__(self, message):
        super(EmptyLearningData, self).__init__(message)


class TooSmallLearningData(Exception):
    def __init__(self, message):
        super(TooSmallLearningData, self).__init__(message)


class InvalidOrder(Exception):
    def __init__(self, message):
        super(InvalidOrder, self).__init__(message)
