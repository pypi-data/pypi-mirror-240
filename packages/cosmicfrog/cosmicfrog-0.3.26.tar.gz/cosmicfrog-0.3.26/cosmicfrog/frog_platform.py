import os
import json
import logging
import optilogic
import time
from typing import Tuple

# Functions to facilitate interactions with Optilogic platform using 'optilogic' library

class OptilogicClient():
    """
    Wrapper for optilogic module for consumption in Cosmic Frog services
    """
    def __init__(self, username = None, appkey = None, logger = logging.getLogger()):

        # Detect if being run in Andromeda
        job_app_key = os.environ.get('OPTILOGIC_JOB_APPKEY')

        if appkey and not username:
            # Use supplied key
            self.api = optilogic.pioneer.Api(auth_legacy=False, appkey=appkey)  
        elif appkey and username:
            # Use supplied key & name
            self.api = optilogic.pioneer.Api(auth_legacy=False, appkey=appkey, un=username)
        elif job_app_key:
            # Running on Andromeda
            self.api = optilogic.pioneer.Api(auth_legacy=False)
        else:
            raise ValueError("OptilogicClient could not authenticate")

        self.logger = logger

    def model_exists(self, model_name: str) -> bool:
        """
        Returns True if a given model exists, False otherwise
        """
        try:
            return self.api.storagename_database_exists(model_name)
        except Exception as e:
            self.logger.error( f'Exception in cosmicfrog: {e}')
            return False

    def get_connection_string(self, model_name: str) -> Tuple[bool, str]:
        try:
            rv = {"message" : "error getting connection string"}
            if not self.api.storagename_database_exists(model_name):
                return False, ""
            
            connection_info = self.api.sql_connection_info(model_name)

            return True, connection_info['connectionStrings']['url']

        except Exception as e:
            self.logger.error( f'Exception in cosmicfrog: {e}')
            return False, ""
        
   
    def create_model_synchronous(self, model_name: str, model_template: str):
        try:
            new_model = self.api.database_create(name=model_name, template=model_template)

            status = "success"
            rv = {}
            if "crash" in new_model:
                status = "error"
                rv['message'] = json.loads( new_model['response_body'])['message']
                rv['httpStatus'] = new_model['resp'].status_code
            else:
                while not self.api.storagename_database_exists(model_name):
                    self.logger.info(f"creating {model_name}")
                    time.sleep(3.0)
                connections = self.api.sql_connection_info(model_name)
                rv['model'] = new_model
                rv['connection'] = connections

            return status, rv
        
        except Exception as e:
            return "exception", e

