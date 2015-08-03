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
    #        2) /apirest/proyectos/1234/firmantes/ = proyectos-firmantes
    # Los servicios del estilo 'nombre_servicio', quedan como 'nombreservicio'
    
    serviceName = ''
    
    matchObj = re.match(r'^/apirest/([a-z_]+)/(?:[0-9]+)?/?([a-z_]+)?', serv)
    
    if matchObj:
        serviceName = matchObj.group(1)
        aux_obj = matchObj.group(2)
        
        #Elimino los guiones bajo de los nombres de los servicios
        trantab = {ord(c): None for c in '_'}
        serviceName = serviceName.translate(trantab)

        # Si es un servicio compuesto (tipo 2)
        if aux_obj: 
            #Elimino los guiones bajo de los nombres de los servicios
            aux_obj = aux_obj.translate(trantab)
            serviceName += '-' + matchObj.group(2)
             
                    
    return serviceName 
                