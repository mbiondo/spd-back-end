# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestComunicacionPen(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CANT_COMUNICACIONES_PEN = 5298
            
    CODIGO_EXITO = 200
    TIPO = "COMUNICACION_PEN"
    CODIGO_NUM = '0001'  
    TIPO_CAMARA = "Diputados"
    CODIGO_EXP = "0001-JGM-1995"
    CODIGO_ANIO = "2002"
    CODIGO_ANIO_CODIGO_NUM = "1995"
    PERIODO = 113
    CODIGO_ORIGEN = 'JGM'
    CODIGO_ANIO_ORDEN = "2002"
        
    # Test: Servicio de cominicaciones pen
    def test_comunicacion_pen(self):
        """
        Prueba servicio de comunicaciones_pen.  
        """
        response = self.client.get('/apirest/comunicaciones_pen/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_COMUNICACIONES_PEN)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        
    def test_comunicacion_pen_id(self):
        """
        Prueba el servicio para traer una comunicacion_pen por id
        """
        response = self.client.get('/apirest/comunicaciones_pen/1/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["tipo"], self.TIPO)
        self.assertEqual(response.data["tipo_camara"], self.TIPO_CAMARA)
        
    def test_comunicacion_pen_tipo_camara(self):
        """
        Prueba que traiga las comunicaciones_pen filtrando por tipo de camara.
        """
        response = self.client.get('/apirest/comunicaciones_pen/?tipo_camara=Diputados')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)  
        
    def test_comunicacion_pen_codigo_origen(self):
        """
        Prueba que traiga las comunicaciones_pen filtrando por codigo de origen.
        """
        response = self.client.get('/apirest/comunicaciones_pen/?codigo_origen=JGM')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)

    def test_comunicacion_pen_codigo_exp(self):
        """
        Prueba que traiga las comunicaciones_pen filtrando por codigo de expediente.
        """
        response = self.client.get('/apirest/comunicaciones_pen/?codigo_exp=0001-JGM-1995')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXP)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        
    def test_comunicacion_pen_codigo_num(self):
        """
        Prueba que traiga las comunicaciones_pen filtrando por codigo de numero.
        """        
        response = self.client.get('/apirest/comunicaciones_pen/?codigo_num=0001')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXP)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO_CODIGO_NUM)      
        
    def test_comunicacion_pen_periodo(self):
        """
        Prueba que traiga las comunicaciones_pen filtrando por periodo
        """                  
        response = self.client.get('/apirest/comunicaciones_pen/?periodo=113')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
            
    def test_fecha_desde_y_hasta(self):
        """
        Prueba que traiga las comunicaciones_pen que pertenecen al rango de fecha indicada.
        """
        response = self.client.get('/apirest/comunicaciones_pen/?fechaDesde=2015-01-01&fechaHasta=2015-04-01')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        
    def test_comunicacion_pen_subtipo(self):
        """
        Prueba que traiga todas las comunicaciones_pen de un determinado subtipo.
        """
        response = self.client.get('/apirest/comunicaciones_pen/?subtipo=NORMA')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)        
    
    #Test con filtros combinados. 
    def test_codigo_anio_y_codigo_num(self):
        """
        Prueba que traiga las comunicaciones_pen por un anio y numero determinado.
        """
        response = self.client.get('/apirest/comunicaciones_pen/?codigo_num=0001&codigo_anio=2002')   
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)       
        
    def test_codigo_anio_y_subtipo(self):
        """
        Prueba que traiga las comunicaciones_pen por un anio y orden.
        """
        response = self.client.get('/apirest/comunicaciones_pen/?codigo_anio=2002&orden=2')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO_ORDEN)
        
