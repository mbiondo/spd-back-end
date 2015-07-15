#!/usr/bin/env python
import os
import sys
import logging

def run_services():

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ServiciosParlamentarios.settings")
    
    logger = logging.getLogger('apirest')   
    
    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)
    
    logger.info('*** Stopping ServiciosParlamentarios ***')

if __name__ == "__main__":
    run_services()
