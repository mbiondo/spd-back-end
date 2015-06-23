# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestDictamen(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CODIGO_EXITO = 200
    UNO = 1 
    CANT_DICTAMENES = 51498
    CANT_DICTAMENES_POR_DESPACHO = 2
    CANT_DICTAMENES_POR_ACCION = 1706
    CANT_DICTAMENES_POR_TIPO_CAMARA = 51498
    NUMERO = 10
    ID = 48348
    ACCION = "APROBACIÓN"
    
    
    def test_dictamenes(self):
        """
        Prueba que traiga todos los dictamenes 
        """
        response = self.client.get('/apirest/dictamenes/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_DICTAMENES)
        
    def test_dictamen_id(self):
        """
        Prueba que traiga un dictamen por id
        """
        response = self.client.get('/apirest/dictamenes/48348/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["id"], self.ID)
        
    def test_dictamenes_despacho(self):
        """
        Prueba que traiga todos los dictamenes de un despacho. 
        """
        response = self.client.get('/apirest/dictamenes/?despacho_numero=10')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_DICTAMENES_POR_DESPACHO)     
        
    def test_dictamenes_por_accion(self):
        """
        Prueba que traiga todos los dictamenes de una accion
        """
        response = self.client.get('/apirest/dictamenes/?accion=INDETERMINADO')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_DICTAMENES_POR_ACCION)     
        
    def test_dictamenes_por_tipo_camara(self):
        """
        Prueba que traiga todos los dictamenes de un tipo camara
        """
        response = self.client.get('/apirest/dictamenes/?despacho_tipo_camara=D')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_DICTAMENES_POR_TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["despacho"], self.UNO)      
        
    def test_dictamenes_por_tipo_camara_y_accion(self):
        """
        Prueba que traiga todos los dictamenes de un tipo y un tipo de camara.
        Debe cumplir ambas condiciones.
        """    
        response = self.client.get('/apirest/dictamenes/?despacho_tipo_camara=D&accion=INDETERMINADO')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_DICTAMENES_POR_ACCION)