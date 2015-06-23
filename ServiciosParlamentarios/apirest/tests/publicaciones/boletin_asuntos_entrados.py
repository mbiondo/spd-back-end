# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestBoletinAsuntosEntrados(APITestCase):
    
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANTIDAD_BAE = 735
    CANTIDAD_BAE_POR_NUMERO = 16
    NUMERO = 1
    FK_CAMARA_REUNION = 15
    FK_CAMARA_REUNION_ID = 12
    NUMERO_ID = 35
    
    def test_bae_list(self):
        """
        Prueba el servicio para listar los BAE. 
        """
        response = self.client.get('/apirest/boletines_asuntos_entrados/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_BAE)
        
    def test_bae_por_numero(self):
        """
        Prueba el servicio para obtener un BAE filtrando por numero.
        """
        response = self.client.get("/apirest/boletines_asuntos_entrados/?numero=1")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_BAE_POR_NUMERO)
        self.assertEqual(response.data["results"][0]["numero"], self.NUMERO)
        self.assertEqual(response.data["results"][0]["fk_camara_reunion"], self.FK_CAMARA_REUNION)
        
    def test_bae_por_id(self):
        """
        Prueba el servicio para obtener un BAE por id. 
        """
        response = self.client.get("/apirest/boletines_asuntos_entrados/45452/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["numero"], self.NUMERO_ID)
        self.assertEqual(response.data["fk_camara_reunion"], self.FK_CAMARA_REUNION_ID)
       
    def test_bae_por_tipo(self):
        """
        Prueba el servicio para obtener un BAE filtrando por tipo.
        """
        response = self.client.get("/apirest/boletines_asuntos_entrados/?tipo=BOLETIN_ASUNTOS_ENTRADOS")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_BAE)
        