# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestBoletinNovedades(APITestCase):
    
    # LA TABLA NO TIENE DATOS. QUEDAN LOS TESTS COMENTADOS. ACTULIZAR LAS CONSTANTES CUANDO SE COMPLETE LA TABLA.
    
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANTIDAD_BN = 735
    CANTIDAD_BN_POR_NUMERO = 16
    NUMERO = 1
#     TIPO_CAMARA = 
#     
#     def test_bn_list(self):
#         """
#         Prueba el servicio para listar los BN. 
#         """
#         response = self.client.get('/apirest/boletines_novedades/')
#         self.assertEqual(response.status_code, self.CODIGO_EXITO)
#         self.assertEqual(response.data["count"], self.CANTIDAD_BAE)
#         
#     def test_bn_por_numero(self):
#         """
#         Prueba el servicio para obtener un BN filtrando por numero.
#         """
#         response = self.client.get("/apirest/boletines_novedades/?numero=1")
#         self.assertEqual(response.status_code, self.CODIGO_EXITO)
#         self.assertEqual(response.data["count"], self.CANTIDAD_BAE_POR_NUMERO)
#         self.assertEqual(response.data["results"][0]["numero"], self.NUMERO)
#         self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
#         
#     def test_bn_por_id(self):
#         """
#         Prueba el servicio para obtener un BAT por id. 
#         """
#         response = self.client.get("/apirest/boletines_novedades/XXX/")
#         self.assertEqual(response.status_code, self.CODIGO_EXITO)
#         self.assertEqual(response.data["numero"], self.NUMERO)
#         self.assertEqual(response.data["tipo_camara"], self.TIPO_CAMARA)