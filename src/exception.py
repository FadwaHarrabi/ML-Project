import sys
from src.logger import logging
#sys have all information on any exception in the work environnement 
def error_message_detail(error,error_detail:sys):
   #exc_tb have the information on the excetion or the error in which file and in which line
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_messages="Error occured in python script name [{0}] line number [{1}]  error message [{2}]".format()  # noqa: F524
    file_name,exc_tb.tb_lineno,str(error)

    return error_messages


class CustomException(Exception):
    def __init__(self,error_messages,error_detail:sys) :
        super().__init__(error_messages)
        self.error_messages=error_message_detail(error_messages,error_detail=error_detail)

    def __str__(self) :
        return self.error_messages

    
    



    