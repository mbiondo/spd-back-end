# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestPersonaFisica(APITestCase):
     
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANT_PERSONAS = 1530
    NOMBRE = "PEDRO JOSE" 
    APELLIDO = "AZCOITI"
    
    
    def test_personas_fisicas(self):
        """
        Prueba el servicio para listar las personas fisicas. 
        """
        response = self.client.get('/apirest/personas_fisicas/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PERSONAS)
         
    def test_personas_fisicas_nombre(self):
        """
        Prueba el servicio para obtener una persona filtrando por nombre.
        """
        response = self.client.get("/apirest/personas_fisicas/?nombre=pedro jose")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["results"][0]["historico"][0]["nombre"], self.NOMBRE)
        self.assertEqual(response.data["results"][0]["historico"][0]["apellido"], self.APELLIDO)
#            
    def test_personas_fisicas_apellido(self):
        """
        Prueba el servicio para obtener una persona filtrando por apellido.
        """
        response = self.client.get("/apirest/personas_fisicas/?apellido=azcoiti")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["historico"][0]["nombre"], self.NOMBRE)
        self.assertEqual(response.data["results"][0]["historico"][0]["apellido"], self.APELLIDO)        

        
    def test_personas_fisicas_id(self):
        """
        Prueba el servicio para obtener una personas fisicas por id. 
        """
        response = self.client.get("/apirest/personas_fisicas/299/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["historico"][0]["nombre"], self.NOMBRE)
        self.assertEqual(response.data["historico"][0]["apellido"], self.APELLIDO)
        
