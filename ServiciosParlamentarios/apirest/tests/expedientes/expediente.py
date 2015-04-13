# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestExpediente(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CODIGO_EXITO = 200
    CANT_EXPEDIENTES_PROYECTO = 260357
    CANT_EXPEDIENTES_COMUNICACION = 13120
    CANT_EXPEDIENTES_OBSERVACION = 740
    CANT_EXPEDIENTES_COMUNICACION_PEN = 5218
    CANT_EXPEDIENTES_SOLICITUD = 3779
    CANT_RANGO_FECHAS = 111
    CANT_IGUAL_CODIGO_NUM = 158
    CANT_TIPO_CAMARA = 183247
    CANT_EXPEDIENTES_X_FIRMANTE = 1321
    CANT_COMISION = 9164
    TIPO_CAMARA = "Diputados"
    RANGO_FECHAS_VOCES = "26895 DECRETOS DE NECESIDAD Y URGENCIA " 
    TIPO = "COMUNICACION"
    TIPO_PROYECTO = "PROYECTO"
    TIPO_COMUNICACION_PEN = "COMUNICACION_PEN"
    PERIODO = 131
    
    # Test: ATRIBUTOS DE EXPEDIENTE.
    def test_tipo_proyecto(self):
        """
        Prueba que traiga todos los expedientes que son del tipo proyecto. 
        """
        response = self.client.get('/apirest/expedientes/?tipo=PROYECTO')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_EXPEDIENTES_PROYECTO)
    
    def test_tipo_comunicacion(self):
        """
        Prueba que traiga todos los expedientes que son del tipo Comunicacion
        """
        response = self.client.get('/apirest/expedientes/?tipo=COMUNICACION')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_EXPEDIENTES_COMUNICACION)
        
    def test_tipo_observacion(self):
        """
        Prueba que traiga todos los expedientes que son del tipo observacion
        """
        response = self.client.get('/apirest/expedientes/?tipo=OBSERVACION')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_EXPEDIENTES_OBSERVACION)
        
    def test_tipo_comunicacion_pen(self):
        """
        Prueba que traiga todos los expedientes que son del tipo comunicacion pen
        """
        response = self.client.get('/apirest/expedientes/?tipo=COMUNICACION_PEN')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_EXPEDIENTES_COMUNICACION_PEN)
        
    def test_tipo_solicitud(self):
        """
        Prueba que traiga todos los expedientes que son del tipo solicitud
        """
        response = self.client.get('/apirest/expedientes/?tipo=SOLICITUD')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_EXPEDIENTES_SOLICITUD)
        
    def test_fecha_desde_y_hasta(self):
        """
        Prueba que traiga los expedientes que pertenecen al rango de fecha indicada.
        """
        response = self.client.get('/apirest/expedientes/?fechaDesde=2015-01-01&fechaHasta=2015-04-01')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_RANGO_FECHAS)
        self.assertEqual(response.data["results"][0]["tipocamara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["voces"], self.RANGO_FECHAS_VOCES)
      
    def test_codigo_exp(self):
        """
        Prueba que traiga los expedientes que tienen un determinado codigoExp
        """
        response = self.client.get('/apirest/expedientes/?codigoExp=0019-JGM-2014')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["tipocamara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["voces"], self.RANGO_FECHAS_VOCES)
        
    def test_codigo_num(self):
        """
        Prueba que traiga todos los proyectos que tienen igual codigoNum
        """    
        response = self.client.get('/apirest/expedientes/?codigoNum=0019')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_IGUAL_CODIGO_NUM)
        self.assertEqual(response.data["results"][3]["tipocamara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][3]["tipo"], self.TIPO)
        
        
    def test_tipo_camara(self):
        """
        Prueba que traiga los expedientes de un determinado tipo de camara.
        """
        response = self.client.get('/apirest/expedientes/?tipoCamara=Diputados')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipocamara"], self.TIPO_CAMARA)
        
    #Test: TEST DE ATRIBUTOS DE FIRMANTES.
    def test_firmante_id(self):
        """
        Prueba que traiga los expedientes que fueron firmados por un firmante.
        """
        response = self.client.get('/apirest/expedientes/?firm_persona_fisica_id=1566')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_EXPEDIENTES_X_FIRMANTE)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO_PROYECTO)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        
    def test_firm_nombre_leg_func(self):
        """
        Prueba que traiga los expedientes que fueron firmados por un firmante
        """
        response = self.client.get('/apirest/expedientes/?firm_nombre_leg_func=GERARDO RUBEN MORALES')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_EXPEDIENTES_X_FIRMANTE)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO_PROYECTO)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        
    #Test: TEST DE ATRIBUTOS DE COMISION
    def test_giro_comision_id(self):
        """
        Prueba que traiga todos los expedientes en los que participo una comision
        """
        response = self.client.get('/apirest/expedientes/?giro_comision_id=1913')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_COMISION)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO_COMUNICACION_PEN)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        
    def test_giro_comision_nombre(self):
        """
        Prueba que traiga todos los expedientes en los que participo una comision con un determinado nombre
        """    
        response = self.client.get('/apirest/expedientes/?giro_comision_nombre=EDUCACION Y CULTURA')
        self.assertEqual(response.data["count"],self.CANT_COMISION)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO_COMUNICACION_PEN)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        
    def test_and_filtros(self):
        """
        Prueba que traiga todos los expedientes en los que participo una comision con un determinado nombre
        """    
        response = self.client.get('/apirest/expedientes/?tipo=PROYECTO&firm_persona_fisica_id=1566')
        self.assertEqual(response.data["count"],self.CANT_EXPEDIENTES_X_FIRMANTE)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO_PROYECTO)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
    
        