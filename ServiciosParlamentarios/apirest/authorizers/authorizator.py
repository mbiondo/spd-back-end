from rest_framework.response import Response
import urllib2
import json
from apirest.utils.constants import Constants
from ServiciosParlamentarios import settings
from apirest.utils.logger import Logger
from apirest.utils import utils

def has_permission(func):  
    
    def validate(_self, request, **kwargs):
        """
        Allows access only to permitted users.
        """
        if not settings.AUTHENTICATION:
            return func(_self, request, kwargs)
                        
        if Constants().AUTH_HEADER_KEY_CONST not in request.META:
            return Response(data=Constants().NO_HEADER_EXC, status=Constants().NO_PERMISSION_EXC_CODE)

        auth = request.META[Constants().AUTH_HEADER_KEY_CONST]

        if auth.find(Constants().BEARER_KEY) is -1:
            return Response(data=Constants().AUTH_FORMAT_EXCP_STR, status=Constants().MISSING_TOKEN_CODE)

        token = auth.replace(Constants().BEARER_KEY, "")
        
        if Constants().SERVICE_PATH not in request.META:
            return Response(data=Constants().NO_SERVICE_PATH, status=Constants().NO_PERMISSION_EXC_CODE)
         
        serv = request.META[Constants().SERVICE_PATH]
        
        service_name = utils.getServiceName(serv)
        if not service_name:
                #Bad format
                Logger.e(Constants().BAD_FORMAT_ERROR)
            
        http_method_type = request.method.lower()

        # authorization service => has_permission/<service>/<resource>/<method_type>/<token>/
        #               example => has_permission/expedientes/servicios-parlamentarios/get/XMKe9oAxSw1qHNToWwwjOgHzVUlpUS/


        req = urllib2.Request(Constants().HAS_PERMISSION_SERVICE.format(service_name, settings.AUTH_SERVER['RESOURCE_NAME'], http_method_type, token))
        req.add_header(Constants().AUTH_HEADER_KEY,
                        Constants().AUTH_HEADER_CREDENTIALS.format(settings.AUTH_CLIENT_CREDENTIALS['CLIENT_ID'],
                                                                   settings.AUTH_CLIENT_CREDENTIALS['CLIENT_SECRET']))   
        
        try:
            content = json.loads(urllib2.urlopen(req).read())
            authorized = content[Constants().IS_AUTHORIZED_KEY]
        except urllib2.HTTPError as e:
            return Response(data=Constants().NO_PERMISSION_STR, status=e.code)

        if not authorized: 
            return Response(data=Constants().NO_ROL_PERMISSION_STR, status=Constants().NO_ROL_PERMISSION_CODE)
        
        return func(_self, request, kwargs)

    return validate

