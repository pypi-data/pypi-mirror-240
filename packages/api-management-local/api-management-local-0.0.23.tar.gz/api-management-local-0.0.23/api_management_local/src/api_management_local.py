from dotenv import load_dotenv
import json
import os
from circles_local_database_python.connector import Connector
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from circles_local_database_python.connector import Connector
from circles_local_database_python.generic_crud import GenericCRUD
from url_local.url_circlez import OurUrl
from url_local import action_name_enum, entity_name_enum, component_name_enum
from user_context_remote.user_context import UserContext
from src.api_limit import (DEVELOPER_EMAIL,
                               API_MANAGEMENT_LOCAL_PYTHON_COMPONENT_ID,
                               API_MANAGEMENT_LOCAL_PYTHON_COMPONENT_NAME, APILimitsLocal)
import requests
import http
from sdk.src.validate import validate_enviroment_variables

BRAND_NAME = os.getenv('BRAND_NAME')
validate_enviroment_variables()
AUTHENTICATION_API_VERSION = 1

LEFT_SOFT=-1
BETWEEN_SOFT_AND_HARD=0
MORE_THAN_HARD_LIMIT=1
url_circlez = OurUrl()
authentication_login_validate_jwt_url = url_circlez.endpoint_url(
            brand_name=BRAND_NAME,
            environment_name=os.getenv('ENVIRONMENT_NAME'),
            component_name=component_name_enum.ComponentName.AUTHENTICATION.value,
            entity_name=entity_name_enum.EntityName.AUTH_LOGIN.value,
            version=AUTHENTICATION_API_VERSION,
            action_name=action_name_enum.ActionName.VALIDATE_JWT.value
        )
api_management_local_python_code = {
    'component_id': API_MANAGEMENT_LOCAL_PYTHON_COMPONENT_ID,
    'component_name': API_MANAGEMENT_LOCAL_PYTHON_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': DEVELOPER_EMAIL
}
load_dotenv()
logger=Logger.create_logger(object=api_management_local_python_code)
class APIManagmentLocal( GenericCRUD):
    def __init__(self) -> None:
        pass
    
    def get_actual_by_api_type_id_last_x_hours(self, external_user_id: int, api_type_id: int, value: int, unit: str) -> int:
        logger.start(object={'api_type_id': str(api_type_id), 'value': str(value), 'unit': unit})
        connection = Connector.connect("api_call")
        cursor = connection.cursor()

        try:
            query = """
                SELECT COUNT(*)
                FROM api_call_view
                WHERE api_type_id = {} AND external_user_id = {}
                AND TIMESTAMPDIFF({}, created_timestamp, NOW()) <= {}
                AND http_status_code = {}
            """
            http_status_code = http.HTTPStatus.OK.value
            sql=(query.format(api_type_id, external_user_id,unit, value, http_status_code))
            cursor.execute(sql)
            actual_succ_count = cursor.fetchone()[0]
            logger.end(object={'actual_succ_count': actual_succ_count})
            return actual_succ_count
        except Exception as exception:
            logger.exception(object=exception)
            logger.end()
    
    @staticmethod
    def  _get_json_with_only_sagnificant_fields_by_api_type_id( json1:json, api_type_id:int)-> json:
        logger.start(object={'json1':str(json1),'api_type_id':str(api_type_id)})
        connection = Connector.connect("api_type")
        try:
            cursor = connection.cursor()
            query = f"SELECT field_name FROM api_type.api_type_field_view WHERE api_type_id = %s AND field_significant = TRUE"
            cursor.execute(query, (api_type_id,))
            significant_fields = [row[0] for row in cursor.fetchall()]
            data = json.loads(json1)
            filtered_data = {key: data[key] for key in significant_fields if key in data}
            filtered_json = json.dumps(filtered_data)
            logger.end(object={'filtered_json':str(filtered_json)})
            return filtered_json
        except Exception as exception:
            logger.exception(object=exception)
            logger.end()
            
     
     
     
    
    def check_limit  (self,external_user_id:int,api_type_id:int)->int:
        logger.start(object={'external_user_id':external_user_id,'api_type_id':str(api_type_id)})
        api_limit = APILimitsLocal()
        limits = api_limit.get_api_limit_by_api_type_id_external_user_id(api_type_id,external_user_id)
        soft_limit_value=limits[0]
        soft_limit_unit=limits[1]
        hard_limit_value=limits[2]
         # hard_limit_unit=limits[3]
        api_succ = self.get_actual_by_api_type_id_last_x_hours(external_user_id,api_type_id, soft_limit_value, soft_limit_unit)

        if api_succ < soft_limit_value:
            return LEFT_SOFT
        elif  soft_limit_value <= api_succ and api_succ < hard_limit_value  :
            return BETWEEN_SOFT_AND_HARD
        else:
            return MORE_THAN_HARD_LIMIT

        
        
     
     
  
    def  delete_api(external_user_id:int,api_type_id:int,data:str):
        logger.start(object={external_user_id:str(external_user_id),'api_type_id':str(api_type_id),'data': data})
        try:
            check_limit =APIManagmentLocal.check_limit (external_user_id=external_user_id,api_type_id=api_type_id)
            data_j=json.loads(data)    
            
            if check_limit == LEFT_SOFT:     
                requests.delete(data=data_j)
                logger.end()
            elif check_limit == BETWEEN_SOFT_AND_HARD:
                logger.warn("you passed the soft limit")
                logger.end()
            else:
                logger.error("you passed the hard limit")
                logger.end()          
        except Exception as exception:
            logger.exception(object=exception)
            logger.end()
            
    
    def  get_api(external_user_id:int,api_type_id:int,data:str):
        logger.start(object={'api_type_id':str(api_type_id),'data':data})
        try:
            check_limit =APIManagmentLocal.check_limit (external_user_id=external_user_id,api_type_id=api_type_id)
            data_j=json.loads(data)    
            if check_limit ==LEFT_SOFT:
                requests.get(data=data_j)
                logger.end()
            elif check_limit ==BETWEEN_SOFT_AND_HARD:
                logger.warn("you passed the soft limit")
                logger.end()
            else:
                logger.error("you passed the hard limit")
                logger.end()          
        except Exception as exception:
            logger.exception(object=exception)
            logger.end()
            
        
    def  put_api(external_user_id:int,api_type_id:int,data:str):
        logger.start(object={'external_user_id':str(external_user_id),'api_type_id':str(api_type_id), 'data': data})
        try:
            check_limit =APIManagmentLocal.check_limit (external_user_id=external_user_id,api_type_id=api_type_id)
            data_j=json.loads(data)    
            if check_limit ==LEFT_SOFT:
                requests.put(data=data_j)
                logger.end()
            elif check_limit ==BETWEEN_SOFT_AND_HARD:
                logger.warn("you passed the soft limit")
                logger.end()
            else:
                logger.error("you passed the hard limit")
                logger.end()          
        except Exception as exception:
            logger.exception(object=exception)
            logger.end()
            
    def check_cache(self,api_type_id:int,outgoing_body:str):
        connection = Connector.connect("api_call")
        cursor = connection.cursor()
        outgoing_body_significant_fields_hash = hash(APIManagmentLocal._get_json_with_only_sagnificant_fields_by_api_type_id(outgoing_body, api_type_id=str(api_type_id)))   
        query=f"""SELECT  http_status_code,response_body 
                    FROM api_call.api_call_view
                    JOIN api_type.api_type_view ON api_type.api_type_view.api_type_id = api_call.api_call_view.api_type_id
                    WHERE api_call_view.api_type_id= %s AND http_status_code=200
                        AND TIMESTAMPDIFF( MINUTE , api_call.api_call_view.start_timestamp, NOW() ) <= 1
                        AND outgoing_body_significant_fields_hash= %s 
                        AND is_network=TRUE
                    ORDER BY api_call_id DESC LIMIT 1"""
        cursor.execute(query, (api_type_id,outgoing_body_significant_fields_hash))
        arr =cursor.fetchone()
        return arr,outgoing_body_significant_fields_hash
        
        