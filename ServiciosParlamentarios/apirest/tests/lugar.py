# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestLugar(APITestCase):
     
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANT_LUGARES = 16
    LUGAR_NOMBRE = "Sala 1"
    UBICACION = "Anexo A"
    PISO = "Piso 2"
    
     
    def test_lugares(self):
        """
        Prueba el servicio para listar las lugares. 
        """
        response = self.client.get('/apirest/lugares/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_LUGARES)
         
    def test_lugar_nombre(self):
        """
        Prueba el servicio para obtener un lugar filtrando por nombre.
        """
        response = self.client.get("/apirest/lugares/?nombre=Sala 1")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)     
        self.assertEqual(response.data["results"][0]["nombre"], self.LUGAR_NOMBRE)
        self.assertEqual(response.data["results"][0]["ubicacion"], self.UBICACION)
        self.assertEqual(response.data["results"][0]["piso"], self.PISO)
#            
    def test_lugar_id(self):
        """
        Prueba el servicio para obtener una lugar por id. 
        """
        response = self.client.get("/apirest/lugares/1/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["nombre"], self.LUGAR_NOMBRE)
        self.assertEqual(response.data["ubicacion"], self.UBICACION)
        self.assertEqual(response.data["piso"], self.PISO)
        
    def test_por_piso(self):
        """
        Prueba el servicio para obtener una lugar filtrando por piso.
        """
        response = self.client.get("/apirest/lugares/?piso=Piso 2")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["results"][0]["nombre"], self.LUGAR_NOMBRE)
        self.assertEqual(response.data["results"][0]["ubicacion"], self.UBICACION)
        self.assertEqual(response.data["results"][0]["piso"], self.PISO)
        