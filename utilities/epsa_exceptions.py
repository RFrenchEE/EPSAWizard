from enum import Enum

# Error codes enum
class EPSAError(Enum):
    ERROR1 = 0

# Class to extend Exception class
class EPSAException(Exception):
    def __init__(self, message, error_code, *args):
        super().__init__(message)
        self.error_code = error_code
        self.args = args

    def __str__(self) -> str:
        err_str = self.error_string()
        return f"{err_str}\n{super().__str__()}"


    def error_string(self) -> str:
        match self.error_code:
            case EPSAError.ERROR1:
                return f"Error 1 called with args {self.args}"
