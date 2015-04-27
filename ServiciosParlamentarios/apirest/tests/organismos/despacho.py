# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestDespacho(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CODIGO_EXITO = 200
    CANT_DESPACHOS = 49406
    DESPACHO_TIPO = "DICTAMEN"
    DESPACHO_NUMERO = 0
    CANT_TIPO_CAMARA = 0
    
    def test_despachos(self):
        """
        Prueba que traiga todos despachos
        """
        response = self.client.get('/apirest/despachos/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_DESPACHOS)
        
    def test_despacho_por_id(self):
        """
        Prueba que traiga un despacho por su id. 
        """
        response = self.client.get('/apirest/despachos/45028/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["tipo"], self.DESPACHO_TIPO)
        
    def test_despacho_por_numero(self):
        """
        Prueba que traiga un despacho por su numero. 
        """
        response = self.client.get('/apirest/despachos/?numero=1')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.DESPACHO_TIPO)
        
    def test_despacho_por_tipo_camara(self):
        """
        Prueba que traiga los despachos por tipo de camara. 
        """
        response = self.client.get('/apirest/despachos/?tipo_camara=1')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_TIPO_CAMARA)
        

        

        