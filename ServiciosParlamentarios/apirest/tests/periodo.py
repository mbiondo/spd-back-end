# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestPeriodo(APITestCase):
     
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANT_PERIODOS = 38
    NRO_PERIODO = 101
    ANIO_PARLAMENTARIO = 1983
    CANT_PERIODOS_INICIO = 6
    ID_PERIODO_INICIO = 33
    CANT_PERIODOS_FIN = 28
    ID_PERIODO_FIN = 1
    
    def test_periodos(self):
        """
        Prueba el servicio para listar las periodos. 
        """
        response = self.client.get('/apirest/periodos/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PERIODOS)

    def test_periodo_id(self):
        """
        Prueba el servicio para obtener una período por id. 
        """
        response = self.client.get("/apirest/periodos/1/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["nro_periodo"], self.NRO_PERIODO)
        self.assertEqual(response.data["anio_parlamentario"], self.ANIO_PARLAMENTARIO)
    
    def test_periodo_por_nro_periodo(self):
        """
        Prueba el servicio para obtener un periodo segun nro_periodo.
        """
        response = self.client.get("/apirest/periodos/?nro_periodo=101")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)     
        self.assertEqual(response.data["results"][0]["nro_periodo"], self.NRO_PERIODO)
           
    def test_periodo_por_anio_parlamentario(self):
        """
        Prueba el servicio para obtener un periodo segun anio_parlamentario.
        """
        response = self.client.get("/apirest/periodos/?anio_parlamentario=1983")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)     
        self.assertEqual(response.data["results"][0]["nro_periodo"], self.NRO_PERIODO)

    def test_get_periodo_por_fecha_desde(self): 
        """
        Prueba que traiga los periodos a partir de la fecha_inicio. 
        """
        response = self.client.get('/apirest/periodos/?fecha_inicio=2015-01-10') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PERIODOS_INICIO)       
        self.assertEqual(response.data["results"][0]["id"], self.ID_PERIODO_INICIO)

    def test_get_periodos_por_fecha_fin(self): 
        """
        Prueba que traiga los periodos hasta la fecha_fin. 
        """
        response = self.client.get('/apirest/periodos/?fecha_fin=2012-01-10') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PERIODOS_FIN)
        self.assertEqual(response.data["results"][0]["id"], self.ID_PERIODO_FIN)