# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestResultado(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CANT_RESULTADOS = 51381
    CODIGO_EXITO = 200
    RESULTADO = "ARCHIVO"
    TIPO = "RESOLUCION"
   
        
    # Test: Servicio de resultado
    def test_resultados(self):
        """
        Prueba servicio de resultados.  
        """
        response = self.client.get('/apirest/resultados/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_RESULTADOS)
        
    def test_resultado_id(self):
        """
        Prueba el servicio para traer un resultado por id
        """
        response = self.client.get('/apirest/resultados/8060/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["resultado"], self.RESULTADO)
        self.assertEqual(response.data["tipo"], self.TIPO)