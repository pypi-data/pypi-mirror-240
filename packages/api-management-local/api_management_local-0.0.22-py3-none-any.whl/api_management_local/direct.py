  
from dotenv import load_dotenv
import json
import os
from circles_local_database_python.connector import Connector
from logger_local.Logger import Logger
from logger_local.LoggerComponentEnum import LoggerComponentEnum
from circles_local_database_python.connector import Connector
from circles_local_database_python.generic_crud import GenericCRUD
from src.api_call import APICallsLocal
from src.api_management_local import APIManagmentLocal
from src.external_user_id import get_extenal_user_id_by_api_type_id

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
BIGER_HARD=1
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
class Direct(GenericCRUD):
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def try_to_call_api(external_user_id:int,api_type_id:int, endpoint:str, outgoing_body:str, outgoing_header:str)->str:
        logger.start(object={'external_user_id':str(external_user_id),'api_type_id':str(api_type_id),'endpoint':str(endpoint),'outgoing_body':str(outgoing_body),'outgoing_header':str(outgoing_header)})
        api_management=APIManagmentLocal()
        if external_user_id == None:
            external_user_id = get_extenal_user_id_by_api_type_id(api_type_id)
        connection = Connector.connect("api_call")
        cursor = connection.cursor()
        try:
                query=f"""SELECT  http_status_code,response_body FROM api_call.api_call_view
                    JOIN api_type.api_type_view ON api_type.api_type_view.api_type_id = api_call.api_call_view.api_type_id
                    WHERE api_call_view.api_type_id= %s AND http_status_code=200 AND TIMESTAMPDIFF( MINUTE , api_call.api_call_view.start_timestamp, NOW() ) <= 1
                    ORDER BY api_call_id DESC LIMIT 1"""
                cursor.execute(query, (api_type_id,))
                arr =cursor.fetchone()
                if arr==None:
                    check=api_management.check_limit (external_user_id=external_user_id,api_type_id=api_type_id)
                    logger.info("check= " +str(check))
                    if check!=BIGER_HARD:
                        # user=UserContext.login_using_user_identification_and_password()
                        # data = {"jwtToken":f"Bearer ${user.get_user_JWT()} "}
                        outgoing_body_significant_fields_hash = hash(APIManagmentLocal._get_json_with_only_sagnificant_fields_by_api_type_id(outgoing_body, api_type_id=str(api_type_id)))   
                        output = requests.post(url=endpoint, data=outgoing_body, headers=outgoing_header)
                        status_code=output.status_code
                        text=output.text
                        incoming_message = output.content.decode('utf-8')
                        response_body=output.json()
                        res=json.dumps(response_body)  
                        data1 = (external_user_id,api_type_id,endpoint, outgoing_header, outgoing_body,str(outgoing_body_significant_fields_hash),incoming_message,status_code,res )
                        APICall1=APICallsLocal()
                        api_call_id=APICall1._insert_api_call_tuple(data1)
                        logger.end("check= " +str(check), object={'status_code':status_code,'text':text})
                        return {'status_code':status_code,'text':text}                                  
                    else:
                        logger.error("you passed the hard limit")
                        raise Exception("you passed the hard limit")
                else:
                    status_code=arr[0]
                    text=arr[1]
                    logger.info("bringing result from cache in database", object={status_code,text})
                    return status_code,text
                

                  
        except Exception as exception:
            logger.exception(object=exception)
            logger.end()
            
