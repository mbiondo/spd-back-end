# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestOrdenDia(APITestCase):
     
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    NUMERO = 120
    CANTIDAD_ODS = 45171
    CANTIDAD_ODS_ID = 1
    CANTIDAD_ODS_POR_NUMERO = 23
    TIPO = "ORDEN_DIA" 
     
    def test_od_list(self):
        """
        Prueba el servicio para listar las OD. 
        """
        response = self.client.get('/apirest/orden_dia/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_ODS)
         
    def test_od_por_numero(self):
        """
        Prueba el servicio para obtener un OD filtrando por numero.
        """
        response = self.client.get("/apirest/orden_dia/?numero=120")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_ODS_POR_NUMERO)
        self.assertEqual(response.data["results"][0]["numero"], self.NUMERO)
          
    def test_od_por_id(self):
        """
        Prueba el servicio para obtener un OD por id. 
        """
        response = self.client.get("/apirest/orden_dia/1/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["numero"], self.NUMERO)
        self.assertEqual(response.data["tipo"], self.TIPO)
        
    def test_od_por_numero_y_anio(self):
        """
        Prueba el servicio para obtener un OD filtrando por numero.
        """
        response = self.client.get("/apirest/orden_dia/?numero=120&anio=2010")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["numero"], self.NUMERO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        