# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestComision(APITestCase):
    
    CANT_COMISIONES_PERMANENTES_2014 = 45
    INTEGRANTES_TURISMO_2014 = 31
    
    def test_get_comisiones(self):
        """
        Prueba que se obtengan todas las comisiones
        """        
        response = self.client.get('/apirest/comisiones_detalle/?fecha=2014-10-10&tipo_camara=CD&page=3&caracter=P')        
        self.assertEqual(response.data["count"], self.CANT_COMISIONES_PERMANENTES_2014)

    def test_integrantes_comision_turismo_2014(self):
        """
        Prueba que la Comision de Turisimo tenga el numero correcto de integrantes
        """        
        response = self.client.get('/apirest/comisiones_detalle/?fecha=2014-10-10&tipo_camara=CD&nombre=TURISMO')        
        self.assertEqual(len(response.data["results"][0]["integrantes"]), self.INTEGRANTES_CULTURA_2014)