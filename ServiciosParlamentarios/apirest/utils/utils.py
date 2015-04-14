import re

def singleton(class_):
    
    instances = {}
    
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
  
    return getinstance            

def getServiceName(serv):
    
    #Regex para parsear la URL del servicio solicitado
    #Ejemplo: 
    #        1) /apirest/cargos/ => serviceName = cargos
    #        2) /apirest/expedientes/1234/firmantes/ = expedientes-firmantes
    
    serviceName = ''
    
    matchObj = re.match(r'^/apirest/([a-z]+)/(?:[0-9]+)?/?([a-z]+)?', serv)
    
    if matchObj:
        serviceName = matchObj.group(1)
        aux_obj = matchObj.group(2)
        if aux_obj:
            serviceName += '-' + matchObj.group(2) 
                    
    return serviceName 
                