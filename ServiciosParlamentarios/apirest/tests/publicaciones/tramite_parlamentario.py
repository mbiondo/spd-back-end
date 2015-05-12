# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestTramiteParlamentario(APITestCase):
    
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANTIDAD_TPS = 2450
    CANTIDAD_TPS_POR_NUMERO = 16
    NUMERO = 1
    FK_BOLETIN = 45382
    
    def test_tp_list(self):
        """
        Prueba el servicio para listar los tramites parlamentarios. 
        """
        response = self.client.get('/apirest/tramites_parlamentarios/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_TPS)
        
    def test_tp_por_numero(self):
        """
        Prueba el servicio para obtener un tramite filtrando por numero.
        """
        response = self.client.get("/apirest/tramites_parlamentarios/?numero=1")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANTIDAD_TPS_POR_NUMERO)
        self.assertEqual(response.data["results"][0]["numero"], self.NUMERO)
        self.assertEqual(response.data["results"][0]["fk_boletin_asuntos_entrados"], self.FK_BOLETIN)
        
    def test_tp_por_id(self):
        """
        Prueba el servicio para obtener un tp por id. 
        """
        response = self.client.get("/apirest/tramites_parlamentarios/45907/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["numero"], self.NUMERO)
        self.assertEqual(response.data["fk_boletin_asuntos_entrados"], self.FK_BOLETIN)
        
        