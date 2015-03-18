from rest_framework.response import Response
from rest_framework.permissions import BasePermission
import urllib2
import json
import httplib
from apirest.utils.constants import Constants
from ServiciosParlamentarios import settings
from apirest.exceptions.authorizationErrors import ServerAuthConnectionException,\
    NoAuthorizationException, AuthorizationFormatException,\
    NotAuthorizedException
from apirest.utils.logger import Logger

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

class HasPermission(BasePermission):
    """
    Allows access only to permitted users.
    """
    _BEARER_KEY="Bearer "
    _AUTH_HEADER_KEY='HTTP_AUTHORIZATION'
    _AUTH_HEADER_VALUE='Authenticator Host: {0}:{1} - Token: {2}'
    _IS_VALID_KEY='is_valid'
    _VALIDATE_TOKEN_URL='/o/validate_token/{0}/'
    _HEADER_CREDENTIAL_FORMAT='Credential {0} {1}'    

    def gte_validation_data(self, token):
        
        try:
            Logger().d(self._AUTH_HEADER_VALUE.format(settings.AUTH_SERVER['HOST'], settings.AUTH_SERVER['PORT'], token))
            cnn = httplib.HTTPConnection('{0}:{1}'.format(settings.AUTH_SERVER['HOST'], settings.AUTH_SERVER['PORT']))
            cnn.request("GET", self._VALIDATE_TOKEN_URL.format(token), headers={'AUTHORIZATION':self._HEADER_CREDENTIAL_FORMAT.format(settings.AUTH_CLIENT_CREDENTIALS['CLIENT_ID'], settings.AUTH_CLIENT_CREDENTIALS['CLIENT_SECRET'])})
            data = json.loads(cnn.getresponse().read())
            cnn.close()
            return data
        except Exception as e:
            print str(e)
            raise ServerAuthConnectionException()
        

    def has_permission(self, request, view):
        
        if settings.AUTHENTICATION is False:
            return True
        
        if self._AUTH_HEADER_KEY not in request.META:
            raise NoAuthorizationException()  
        
        auth = request.META[self._AUTH_HEADER_KEY]
        
        if auth.find(self._BEARER_KEY) is -1:
            raise AuthorizationFormatException()
        
        token = auth.lstrip(self._BEARER_KEY)
        
        #asks oauth2 for token permissions
        valid = self.validate(self.gte_validation_data(token)) 

        if not valid:
            raise NotAuthorizedException() 
        
        Logger().d("Authentication successful.")
        return True 
    
    def validate(self, data):
        return data[self._IS_VALID_KEY] if self._IS_VALID_KEY in data else False


def hand_unauthorized_exc(func):
        def unauthorized_handler(_self, exc): 
            if isinstance(exc, (AuthorizationFormatException, NoAuthorizationException, NotAuthorizedException, ServerAuthConnectionException)):
                return Response(data=exc.default_detail, status=exc.status_code, exception=True)
            
            return func(_self, exc)
            
        return unauthorized_handler
        