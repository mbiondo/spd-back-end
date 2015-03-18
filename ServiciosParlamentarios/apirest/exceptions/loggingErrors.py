from apirest.utils.constants import Constants

class LoggingFolderException(Exception):
    
    default_detail = Constants().LOGGING_FOLDER_EXC
    
    def __init__(self):
        Exception.__init__(self, Constants().LOGGING_FOLDER_EXC)
        


