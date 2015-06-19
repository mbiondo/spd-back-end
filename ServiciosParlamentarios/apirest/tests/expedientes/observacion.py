# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestObservacion(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CANT_OBSERVACIONES = 769

    CODIGO_EXITO = 200
    TIPO = "OBSERVACION"
    CODIGO_NUM = '0001'  
    TIPO_CAMARA = "Diputados"
    CODIGO_EXP = "0001-ODA-2013"
    CODIGO_ANIO = "2013"
    PERIODO = 115
    CODIGO_ORIGEN = 'ODA'
    CODIGO_ANIO_ORDEN = "2002"
        
    # Test: Servicio de observaciones
    def test_observacion(self):
        """
        Prueba servicio de comunicaciones.  
        """
        response = self.client.get('/apirest/observaciones/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_OBSERVACIONES)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        
    def test_observacion_id(self):
        """
        Prueba el servicio para traer una comunicacion por id
        """
        response = self.client.get('/apirest/observaciones/278007/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["tipo"], self.TIPO)
        self.assertEqual(response.data["tipo_camara"], self.TIPO_CAMARA)
        
    # Test sobre filtros. 
        
    def test_observacion_tipo_camara(self):
        """
        Prueba que traiga las comunicaciones filtrando por tipo de camara.
        """
        response = self.client.get('/apirest/observaciones/?tipo_camara=Diputados')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)  
        
    def test_observacion_codigo_origen(self):
        """
        Prueba que traiga las comunicaciones filtrando por codigo de origen.
        """
        response = self.client.get('/apirest/observaciones/?codigo_origen=ODA')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)

    def test_observacion_codigo_exp(self):
        """
        Prueba que traiga las comunicaciones filtrando por codigo de expediente.
        """
        response = self.client.get('/apirest/observaciones/?codigo_exp=0001-ODA-2013')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXP)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        
    def test_comunicacion_codigo_num(self):
        """
        Prueba que traiga las comunicaciones filtrando por codigo de numero.
        """        
        response = self.client.get('/apirest/observaciones/?codigo_num=0001')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXP)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO)      
            
    def test_fecha_desde_y_hasta(self):
        """
        Prueba que traiga las comunicaciones que pertenecen al rango de fecha indicada.
        """
        response = self.client.get('/apirest/observaciones/?fechaDesde=2015-01-01&fechaHasta=2015-04-01')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        
    def test_observacion_despacho(self):
        """
        Prueba que traiga todas las comunicaciones de un determinado subtipo.
        """
        response = self.client.get('/apirest/observaciones/?subtipo=PASE A DIPUTADOS')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)        
        
    def test_observacion_orden(self):
        """
        Prueba que traiga todas las comunicaciones de un determinado orden.
        """
        response = self.client.get('/apirest/observaciones/?orden=2')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
    
    #Test con filtros combinados. 
    def test_codigo_anio_y_codigo_num(self):
        """
        Prueba que traiga las comunicaciones por un anio y numero determinado.
        """
        response = self.client.get('/apirest/observaciones/?codigo_num=0001&codigo_anio=2013')   
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)       
        
    def test_codigo_anio_y_orden(self):
        """
        Prueba que traiga las comunicaciones por un anio y orden.
        """
        response = self.client.get('/apirest/observaciones/?codigo_anio=2002&orden=2')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO_ORDEN)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)     
        
