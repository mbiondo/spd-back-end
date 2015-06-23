# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestDespacho(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CODIGO_EXITO = 200
    CANT_DESPACHOS = 49801
    TIPO = "DICTAMEN"
    CANT_NUMERO=4339
    NUMERO = 0
    CANT_TIPO_CAMARA = 23287
    TIPO_CAMARA = "Senado"
    
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
        response = self.client.get('/apirest/despachos/45417/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["tipo"], self.TIPO)
        
    def test_despacho_por_numero(self):
        """
        Prueba que traiga un despacho por su numero. 
        """
        response = self.client.get('/apirest/despachos/?numero=0')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["numero"], self.NUMERO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        
    def test_despacho_por_tipo_camara(self):
        """
        Prueba que traiga los despachos por tipo de camara. 
        """
        response = self.client.get('/apirest/despachos/?tipo_camara=senado')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        

        

        