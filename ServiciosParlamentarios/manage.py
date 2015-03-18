#!/usr/bin/env python
import os
import sys
from apirest.utils.logger import Logger
from apirest.exceptions.loggingErrors import LoggingFolderException

def run_services():
    
    try:
        Logger().init()
    except LoggingFolderException as e:
        print e.default_detail
        return
        
    Logger().i('*** Starting ServiciosParlamentarios ***')
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ServiciosParlamentarios.settings")
    
    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)
    
    ''' Stop the logging thread '''
    Logger().i('*** Stopping ServiciosParlamentarios ***')
    Logger().stop()

if __name__ == "__main__":
    run_services()
