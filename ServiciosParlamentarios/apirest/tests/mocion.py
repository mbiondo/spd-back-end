# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestMocion(APITestCase):
     
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANT_MOCIONES = 15549
    CANT_MOCIONES_ORDEN = 163
    MOCION_DESCRIPCION = "MOCION CAMARA EN COMISION (AFIRMATIVA)"
    MOCION_TIPO = "PREFERENCIA"
    MOCION_DESCRIPCION_2 = "MOCION DE PREFERENCIA PARA LA PROXIMA SESION CON DICTAMEN (AFIRMATIVA)" 
    MOCION_RESULTADO = "AFIRMATIVA"
    CANT_MOCIONES_SIN_DICTAMEN = 101
    MOCION_DICTAMEN = "CON O SIN DICTAMEN"
     
    def test_mociones(self):
        """
        Prueba el servicio para listar las mociones. 
        """
        response = self.client.get('/apirest/mociones/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_MOCIONES)
         
    def test_mocion_tipo(self):
        """
        Prueba el servicio para obtener una mocion filtrando por tipo.
        """
        response = self.client.get("/apirest/mociones/?tipo=orden")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_MOCIONES_ORDEN)     
        self.assertEqual(response.data["results"][0]["descripcion"], self.MOCION_DESCRIPCION)
#            
    def test_mocion_id(self):
        """
        Prueba el servicio para obtener una lugar por id. 
        """
        response = self.client.get("/apirest/mociones/1/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["tipo"], self.MOCION_TIPO)
        self.assertEqual(response.data["descripcion"], self.MOCION_DESCRIPCION_2)
        self.assertEqual(response.data["resultado"], self.MOCION_RESULTADO)
        
    def test_por_dictamen(self):
        """
        Prueba el servicio para obtener una mocion filtrando por dictamen.
        """
        response = self.client.get("/apirest/mociones/?dictamen=SIN")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["count"], self.CANT_MOCIONES_SIN_DICTAMEN) 
        self.assertEqual(response.data["results"][0]["tipo"], self.MOCION_TIPO)
        self.assertEqual(response.data["results"][0]["resultado"], self.MOCION_RESULTADO)
        self.assertEqual(response.data["results"][0]["dictamen"], self.MOCION_DICTAMEN)
        