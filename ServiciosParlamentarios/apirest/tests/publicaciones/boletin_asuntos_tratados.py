# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestBoletinAsuntosTratados(APITestCase):
    
    # POR EL MOMENTO QUEDAN COMENTADOS LOS TEST DADO QUE NO HAY DATOS EN LA BASE DE DATOS. AL EXISTIR LOS DATOS 
    # CORRECTOS ES NECESARIO ACTUALIZAR EL VALOR DE LAS CONSTATES.
    
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANTIDAD_BAT = 735
    CANTIDAD_BAT_POR_NUMERO = 16
    NUMERO = 1
    FK_CAMARA_REUNION = 15
    
#     def test_bat_list(self):
#         """
#         Prueba el servicio para listar los BAT. 
#         """
#         response = self.client.get('/apirest/boletin_asuntos_tratados/')
#         self.assertEqual(response.status_code, self.CODIGO_EXITO)
#         self.assertEqual(response.data["count"], self.CANTIDAD_BAT)
        
#     def test_bat_por_numero(self):
#         """
#         Prueba el servicio para obtener un BAT filtrando por numero.
#         """
#         response = self.client.get("/apirest/boletin_asuntos_tratados/?numero=1")
#         self.assertEqual(response.status_code, self.CODIGO_EXITO)
#         self.assertEqual(response.data["count"], self.CANTIDAD_BAT_POR_NUMERO)
#         self.assertEqual(response.data["results"][0]["numero"], self.NUMERO)
#         
#     def test_bat_por_id(self):
#         """
#         Prueba el servicio para obtener un bat por id. 
#         """
#         response = self.client.get("/apirest/boletin_asuntos_tratados/XXXX/")
#         self.assertEqual(response.status_code, self.CODIGO_EXITO)
#         self.assertEqual(response.data["numero"], self.NUMERO)