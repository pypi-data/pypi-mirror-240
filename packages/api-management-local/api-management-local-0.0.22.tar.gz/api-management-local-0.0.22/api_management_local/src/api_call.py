from dotenv import load_dotenv
import json
from typing import Dict
import ast
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from circles_local_database_python.generic_crud import GenericCRUD
from src.api_limit import (
    DEVELOPER_EMAIL,
    API_MANAGEMENT_LOCAL_PYTHON_COMPONENT_ID,
    API_MANAGEMENT_LOCAL_PYTHON_COMPONENT_NAME)

api_management_local_python_code = {
    "component_id": API_MANAGEMENT_LOCAL_PYTHON_COMPONENT_ID,
    "component_name": API_MANAGEMENT_LOCAL_PYTHON_COMPONENT_NAME,
    "component_category": LoggerComponentEnum.ComponentCategory.Code.value,
    "developer_email": DEVELOPER_EMAIL,
}
load_dotenv()

logger = Logger.create_logger(object=api_management_local_python_code)


class APICallsLocal(GenericCRUD):
    def __init__(self) -> None:
        super().__init__(schema_name="api_call",default_table_name="api_call_table")

    def _insert_api_call_tuple(self, api_call_data_tuple: tuple) -> int:
        api_call_data_dict  = {
            'external_user_id':api_call_data_tuple[0],
            'api_type_id': api_call_data_tuple[1],
            'endpoint': api_call_data_tuple[2],
            'outgoing_header': str(api_call_data_tuple[3]),
            'outgoing_body': api_call_data_tuple[4],
            'outgoing_body_significant_fields_hash': api_call_data_tuple[5],
            'incoming_message': api_call_data_tuple[6],
            'http_status_code': api_call_data_tuple[7],
            'response_body': api_call_data_tuple[8],
        }
        logger.start(object={"api_call_data_dict ": api_call_data_dict })
        try:
            api_call_data_json_dumps = json.dumps(api_call_data_dict)  
            api_call_data_json = json.loads(api_call_data_json_dumps)   
            api_call_id=self.insert(json_data=api_call_data_json)
            logger.end()
            return api_call_id
        except Exception as exception:
            logger.exception(object=exception)
            logger.end()
            
