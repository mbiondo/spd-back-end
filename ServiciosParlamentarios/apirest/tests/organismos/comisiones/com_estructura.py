# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestComEstructura(APITestCase):
    
    CODIGO_EXITO = 200
    CANT_LEG_COM = 3955
    CARGO = "presidente"
    JERARQUIA = 1 
    FK_COMISION = 33
    FK_LEGISLADOR_1 = 1714
    FK_LEGISLADOR_2 = 949
    CANT_COMISION_33 = 91
    CANT_COMISION_IDS = 3
    CANT_ESTRUCTURAS_DESDE = 77
    ID_FECHA_DESDE = 1130
    CANT_ESTRUCTURAS_HASTA = 1559
    ID_FECHA_HASTA = 1276
    CANT_ESTRUCTURAS_CARGO = 396
    ID_CARGO = 365
    
    def test_get_legisladores_comisiones(self):
        """
        Prueba que se obtengan todos los legisladores de las comisiones.
        """        
        response = self.client.get('/apirest/legisladores_comisiones/')        
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_LEG_COM)
        
    def test_get_legisladores_comisiones_id(self):
        """
        Prueba que traiga una comision legisladores por id.
        """
        response = self.client.get('/apirest/legisladores_comisiones/364/') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["cargo"], self.CARGO)
        self.assertEqual(response.data["jerarquia"], self.JERARQUIA)
        self.assertEqual(response.data["fk_comision"],self.FK_COMISION)
        self.assertEqual(response.data["fk_legislador"],self.FK_LEGISLADOR_1)


    def test_get_legisladores_comisiones_por_comision_id(self): 
        """
        Prueba que traiga las estructuras en base al filtro de comision_id. 
        """
        response = self.client.get('/apirest/legisladores_comisiones/?comision_id=33') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_COMISION_33)
        self.assertEqual(response.data["results"][0]["fk_comision"], self.FK_COMISION)
        self.assertEqual(response.data["results"][0]["fk_legislador"],self.FK_LEGISLADOR_2)

    def test_get_legisladores_comisiones_por_ids(self): 
        """
        Prueba que traiga las 3 estructuras solicitadas por id. 
        """
        response = self.client.get('/apirest/legisladores_comisiones/?id=1,2,3') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_COMISION_IDS)
    
    def test_get_legisladores_comisiones_por_fecha_desde(self): 
        """
        Prueba que traiga las estructuras a partir de la fecha_desde. 
        """
        response = self.client.get('/apirest/legisladores_comisiones/?fecha_desde=2015-01-10') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_ESTRUCTURAS_DESDE)       
        self.assertEqual(response.data["results"][0]["id"], self.ID_FECHA_DESDE)

    def test_get_legisladores_comisiones_por_fecha_hasta(self): 
        """
        Prueba que traiga las estructuras a partir de la fecha_hasta. 
        """
        response = self.client.get('/apirest/legisladores_comisiones/?fecha_hasta=2012-01-10') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_ESTRUCTURAS_HASTA)
        self.assertEqual(response.data["results"][0]["id"], self.ID_FECHA_HASTA)

    def test_get_legisladores_comisiones_por_cargo(self): 
        """
        Prueba que traiga las estructuras aplicando el filtro de cargo. 
        """
        response = self.client.get('/apirest/legisladores_comisiones/?cargo=presidente') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_ESTRUCTURAS_CARGO)
        self.assertEqual(response.data["results"][0]["id"], self.ID_CARGO)        
        