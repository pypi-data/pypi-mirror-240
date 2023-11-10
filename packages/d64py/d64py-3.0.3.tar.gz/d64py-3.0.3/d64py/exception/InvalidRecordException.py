#======================================================================
# InvalidRecordException.py
#======================================================================
class InvalidRecordException(BaseException):

    def __init__(self, message):
        super("Invalid or deleted VLIR record requested.")
