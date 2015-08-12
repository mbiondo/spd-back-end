# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestComisionReunion(APITestCase):
    
    CODIGO_EXITO = 200
    CANT_PARTES = 4296
    ART108PARL = "N"
    PARTE_ID = 1 
    DEBATE_ID = 9878
    CANT_PARTES_ART108 = 4296   
    
    def test_get_partes(self):
        """
        Prueba que se obtengan todos los partes.
        """        
        response = self.client.get('/apirest/partes/')        
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PARTES)
        
    def test_get_parte_id(self):
        """
        Prueba que traiga un parte por id.
        """
        response = self.client.get('/apirest/partes/1/') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["art108par1"], self.ART108PARL)
        self.assertEqual(response.data["id"], self.PARTE_ID)
        self.assertEqual(response.data["debate_comision_reunion"][0]["id"],self.DEBATE_ID)


    def test_get_parte_por_art108(self):
        """
        Prueba que traiga los partes en base al filtro por articulo 108. 
        """
        response = self.client.get('/apirest/partes/?art108par1=N')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PARTES_ART108)
        self.assertEqual(response.data["results"][0]["art108par1"], self.ART108PARL)
        self.assertEqual(response.data["results"][0]["debate_comision_reunion"][0]["id"],self.DEBATE_ID)
        
        