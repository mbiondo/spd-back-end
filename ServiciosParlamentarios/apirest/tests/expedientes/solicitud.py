# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestSolicitud(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CANT_SOLICITUD = 11532
    CANT_SUB_TIPO = 4058
    CODIGO_EXITO = 200
    CODIGO_EXPEDIENTE = "2932-D-2015"
    SUB_TIPO = "COFIRMA"
        
    # Test: Servicio de solicitudes
    def test_solicitud(self):
        """
        Prueba servicio de solicitud.  
        """
        response = self.client.get('/apirest/solicitudes/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_SOLICITUD)
        
    def test_solicitud_id(self):
        """
        Prueba el servicio para traer un solicitud por id
        """
        response = self.client.get('/apirest/solicitudes/279116/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["codigo_exp"], self.CODIGO_EXPEDIENTE)
        self.assertEqual(response.data["subtipo"], self.SUB_TIPO)
        
    #Filtros: 
    def test_solicitud_subtipo(self):
        """
        Prueba el servicio para traer un solicitud por id
        """
        response = self.client.get('/apirest/solicitudes/?subtipo=COFIRMA')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_SUB_TIPO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXPEDIENTE)
        self.assertEqual(response.data["results"][0]["subtipo"], self.SUB_TIPO)
        
    #Filtros de expediente
    def test_solicitud_codigo_exp(self):
        """
        Prueba el servicio para traer un solicitud por codigo de expediente
        """ 
        response = self.client.get('/apirest/solicitudes/?codigo_exp=2932-D-2015')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXPEDIENTE)
        self.assertEqual(response.data["results"][0]["subtipo"], self.SUB_TIPO)
        
        
    