# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestResultado(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CANT_RESULTADOS_APROBACION_SIMPLE = 44763
    CODIGO_EXITO = 200
    ID = 1   
        
    # Test: Servicio de resultado
    def test_resultados_aprobaciones_simples(self):
        """
        Prueba servicio de resultados aprobaciones simples.  
        """
        response = self.client.get('/apirest/aprobaciones_simples/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_RESULTADOS_APROBACION_SIMPLE)
        
    def test_resultado_id(self):
        """
        Prueba el servicio para traer un resultado aprociones simple por id
        """
        response = self.client.get('/apirest/aprobaciones_simples/1/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["id"], self.ID)