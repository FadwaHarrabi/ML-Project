import sys
from src.logger import logging
#sys have all information on any exception in the work environnement 
def error_message_detail(error_message, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error_message)
    )
    return error_message


class CustomException(Exception):
    def __init__(self,error_messages,error_detail:sys) :
        super().__init__(error_messages)
        self.error_messages=error_message_detail(error_messages,error_detail=error_detail)

    def __str__(self) :
        return self.error_messages

    
    



    