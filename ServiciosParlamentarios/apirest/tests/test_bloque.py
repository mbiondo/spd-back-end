# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestBloque(APITestCase):
        
    CANT_BLOQUES = 219
    NOMBRE_BLOQUE = "FRENTE PARA LA VICTORIA - PJ"
    TIPO_CAMARA = "D"
    CANT_INTEGRANTES_TOTALES = 382
    CANT_BLOQUES_JUSTICIALISTA = 13
    CANT_BLOQUES_JUSTICIALISTA_2014 = 4
    CANT_BLOQUES_FECHA_2014 = 34
    CANT_INTEGRANTES_FPV_2014 = 119
    
    def test_get_bloques(self):
        """
        Prueba que se obtengan todos los bloques
        """        
        response = self.client.get('/apirest/bloques/')        
        self.assertEqual(response.data["count"], self.CANT_BLOQUES)
        
    def test_get_bloque(self):
        """
        Prueba que se obtengan los datos correctos de un bloque
        """        
        response = self.client.get('/apirest/bloques_detalle/317/')
        integrantes_len = len(response.data["integrantes"])

        self.assertEqual(response.data["nombre"], self.NOMBRE_BLOQUE)
        self.assertEqual(response.data["tipocamara"], self.TIPO_CAMARA)
        self.assertEqual(integrantes_len, self.CANT_INTEGRANTES_TOTALES)
        
    def test_get_bloque_integrantes(self):
        """
        Prueba que se obtengan los datos correctos de un bloquey sus integrantes actuales.
        """        
        response = self.client.get('/apirest/bloques_detalle/?nombre=frente para la victoria&fecha=2014-10-10&tipo_camara=D')
        integrantes_len = len(response.data["results"][0]["integrantes"])
            
        self.assertEqual(response.data["results"][0]["nombre"], self.NOMBRE_BLOQUE)
        self.assertEqual(response.data["results"][0]["tipocamara"], self.TIPO_CAMARA)
        self.assertEqual(integrantes_len, self.CANT_INTEGRANTES_FPV_2014)        

    def test_bloque_filter(self):
        """
        Prueba que el filtro de nombre funcione correctamenet
        """
        response = self.client.get('/apirest/bloques/?nombre=justicialista')
        self.assertEqual(response.data["count"], self.CANT_BLOQUES_JUSTICIALISTA)

    def test_bloque_filter_date(self):
        """
        Prueba que el filtro de fecha y tipo de camara funcionen correctamente
        """
        response = self.client.get('/apirest/bloques_detalle/?fecha=2014-01-01&tipo_camara=D')
        self.assertEqual(response.data["count"], self.CANT_BLOQUES_FECHA_2014)

    def test_bloque_filter_name_date(self):
        """
        Prueba que el filtro de nombre y fecha funcionen correctamente
        """
        response = self.client.get('/apirest/bloques/?nombre=justicialista&fecha=2014-01-01')
        self.assertEqual(response.data["count"], self.CANT_BLOQUES_JUSTICIALISTA_2014)

        
                
        