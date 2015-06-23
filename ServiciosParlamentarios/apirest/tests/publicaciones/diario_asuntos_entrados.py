# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestDiarioAsuntosEntrados(APITestCase):
    
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANTIDAD_DAE = 3319
    CANTIDAD_DAE_POR_NUMERO = 28
    NUMERO = 1

    def test_bn_list(self):
        """
        Prueba el servicio para listar los BN. 
        """
        response = self.client.get('/apirest/diarios_asuntos_entrados/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_DAE)

    def test_bn_por_numero(self):
        """
        Prueba el servicio para obtener un BN filtrando por numero.
        """
        response = self.client.get("/apirest/diarios_asuntos_entrados/?numero=1")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_DAE_POR_NUMERO)
        self.assertEqual(response.data["results"][0]["numero"], self.NUMERO)
         
    def test_bn_por_id(self):
        """
        Prueba el servicio para obtener un BN por id. 
        """
        response = self.client.get("/apirest/diarios_asuntos_entrados/46188/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["numero"], self.NUMERO)