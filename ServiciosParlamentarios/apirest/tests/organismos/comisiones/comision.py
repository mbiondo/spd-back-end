# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestComision(APITestCase):
     
    CODIGO_EXITO = 200
    CANT_COMISIONES = 185
    CARACTER = "P"
    TIPO_CAMARA = "CD"
    FECHA_INICIO = "1983-12-10"
    COMISION_HISTORICA_NOMBRE = "ASUNTOS CONSTITUCIONALES"
    COMISION_NOMBRE= "PRESUPUESTO Y HACIENDA"
    COMISION_ORDEN = 1
    FK_COMISION = 3
    INTEGRANTES_TURISMO_2014 = 31
    CANT_CARACTER = 73
    CANT_NOMBRE_COMISION=2
    CANT_INTEGRANTES_COMISION = 35
     
    def test_get_comisiones(self):
        """
        Prueba que se obtengan todas las comisiones
        """        
        response = self.client.get('/apirest/comisiones/')        
        self.assertEqual(response.data["count"], self.CANT_COMISIONES)
         
    def test_get_comision_id(self):
        """
        Prueba que traiga una comision por id.
        """
        response = self.client.get('/apirest/comisiones/3/') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["caracter"], self.CARACTER)
        self.assertEqual(response.data["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["fecha_inicio"], self.FECHA_INICIO)
        self.assertEqual(response.data["comision_hist"][0]["nombre"], self.COMISION_HISTORICA_NOMBRE)
        self.assertEqual(response.data["comision_hist"][0]["orden"], self.COMISION_ORDEN)
        self.assertEqual(response.data["legisladores"].count(), self.CANT_INTEGRANTES_COMISION)
 
    def test_get_comision_por_caracter(self):
        """
        Prueba que traiga las comisiones en base al filtro por caracter. 
        """
        response = self.client.get('/apirest/comisiones/?caracter=P')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_CARACTER)
        self.assertEqual(response.data["results"][0]["caracter"], self.CARACTER)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["fecha_inicio"], self.FECHA_INICIO)
        self.assertEqual(response.data["results"][0]["comision_hist"][0]["nombre"], self.COMISION_HISTORICA_NOMBRE)
        self.assertEqual(response.data["results"][0]["comision_hist"][0]["orden"], self.COMISION_ORDEN)
        self.assertEqual(response.data["legisladores"].count(), self.CANT_INTEGRANTES_COMISION)
     
    def test_get_tipo_camara(self):
        """
        Prueba que traiga las comisiones en base al filtro de tipo camara.
        """
        response = self.client.get('/apirest/comisiones/?tipo_camara=CD')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_CARACTER)
        self.assertEqual(response.data["results"][0]["caracter"], self.CARACTER)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["fecha_inicio"], self.FECHA_INICIO)
        self.assertEqual(response.data["results"][0]["comision_hist"][0]["nombre"], self.COMISION_HISTORICA_NOMBRE)
        self.assertEqual(response.data["results"][0]["comision_hist"][0]["orden"], self.COMISION_ORDEN)
     
    def test_get_comision_nombre(self):
        """
        Prueba que traiga las comisiones en base al filtro de nombre de comision.
        """
        response = self.client.get('/apirest/comisiones/?nombre=PRESUPUESTO Y HACIENDA')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_NOMBRE_COMISION)
        self.assertEqual(response.data["results"][0]["caracter"], self.CARACTER)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["fecha_inicio"], self.FECHA_INICIO)
        self.assertEqual(response.data["results"][0]["comision_hist"][0]["nombre"], self.COMISION_NOMBRE)     