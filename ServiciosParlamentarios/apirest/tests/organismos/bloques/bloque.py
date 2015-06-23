# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestBloque(APITestCase):
        
    CANT_BLOQUES = 222
    NOMBRE_BLOQUE = "FRENTE PARA LA VICTORIA - PJ"
    TIPO_CAMARA = "D"
    CANT_INTEGRANTES_TOTALES = 382
    CANT_BLOQUES_JUSTICIALISTA = 13
    CANT_BLOQUES_JUSTICIALISTA_2014 = 13
    CANT_BLOQUES_FECHA_2014 = 168
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
        response = self.client.get('/apirest/bloques/170/')

        self.assertEqual(response.data["nombre"], self.NOMBRE_BLOQUE)
        self.assertEqual(response.data["tipo_camara"], self.TIPO_CAMARA)
        
    def test_get_bloque_integrantes(self):
        """
        Prueba que se obtengan los datos correctos de un bloque y sus integrantes actuales.
        """        
        response = self.client.get('/apirest/bloques/?nombre=frente para la victoria&fecha=2014-10-10&tipo_camara=D')
            
        self.assertEqual(response.data["results"][0]["nombre"], self.NOMBRE_BLOQUE)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)     

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
        response = self.client.get('/apirest/bloques/?fecha=2014-01-01&tipo_camara=D')
        self.assertEqual(response.data["count"], self.CANT_BLOQUES_FECHA_2014)

    def test_bloque_filter_name_date(self):
        """
        Prueba que el filtro de nombre y fecha funcionen correctamente
        """
        response = self.client.get('/apirest/bloques/?nombre=justicialista&fecha=2014-01-01')
        self.assertEqual(response.data["count"], self.CANT_BLOQUES_JUSTICIALISTA_2014)

        
                
        