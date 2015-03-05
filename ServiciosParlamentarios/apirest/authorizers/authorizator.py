from rest_framework.response import Response
import urllib2
import json
from apirest.utils.constants import Constants

def has_permission(func):
 
    def validate(_self, request, pk, format=None): 
        """
        Allows access only to permitted users.
        """
        print str(request.META)
        if Constants().AUTH_HEADER_KEY_CONST not in request.META:
            return Response(data=Constants().NO_HEADER_EXC, status=Constants().NO_PERMISSION_EXC_CODE)  
 
        auth = request.META[Constants().AUTH_HEADER_KEY_CONST]
         
        if auth.find(Constants().BEARER_KEY) is -1:
            return Response(data=Constants().AUTH_FORMAT_EXCP_STR, status=Constants().MISSING_TOKEN_CODE) 
        
        token = auth.replace(Constants().BEARER_KEY, "") 
        service_name = _self.__class__.__name__.lower()
        http_method_type = request.method.lower()
        
        req = urllib2.Request(Constants().HAS_PERMISSION_SERVICE.format(service_name, http_method_type, token))
        req.add_header(Constants().AUTH_HEADER_KEY, Constants().AUTH_HEADER_CREDENTIALS.format('5', '1'))

        try:
            content = json.loads(urllib2.urlopen(req).read())
            authorized = content[Constants().IS_AUTHORIZED_KEY]
        except urllib2.HTTPError as e:
            return Response(data=Constants().NO_PERMISSION_STR, status=e.code)

        if not authorized: return Response(data=Constants().NO_ROL_PERMISSION_STR, status=Constants().NO_ROL_PERMISSION_CODE)   
         
        return func(_self, request, pk, format)
         
    return validate    