class ArgError(Exception):
    def __init__(self, message):
        super().__init__(f"missing argument: {message}")

class InvArgError(Exception):
    def __init__(self, message):
        super().__init__(f"invalid argument: {message}")

class InvValError(Exception):
    def __init__(self, message):
        super().__init__(f"invalid argument value: {message}")