# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestComunicacion(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CANT_COMUNICACIONES = 8059
    CANT_TIPO_CAMARA = 4972
    CANT_CODIGO_ORIGEN= 4689
            
    CODIGO_EXITO = 200
    TIPO = "COMUNICACION"
    CODIGO_NUM = '0114'  
    TIPO_CAMARA = "Diputados"
    CODIGO_EXP = "0114-S-1997"
    CODIGO_ANIO = "1997"
    PERIODO = 115
    CODIGO_ORIGEN = 'S'
    CODIGO_ANIO_ORDEN = "2002"
        
    # Test: Servicio de proyectos
    def test_comunicacion(self):
        """
        Prueba servicio de comunicaciones.  
        """
        response = self.client.get('/apirest/comunicaciones/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_COMUNICACIONES)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        
    def test_comunicacion_id(self):
        """
        Prueba el servicio para traer una comunicacion por id
        """
        response = self.client.get('/apirest/comunicaciones/95489/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["tipo"], self.TIPO)
        self.assertEqual(response.data["tipo_camara"], self.TIPO_CAMARA)
        
    # Test sobre filtros. 
        
    def test_comunicacion_tipo_camara(self):
        """
        Prueba que traiga las comunicaciones filtrando por tipo de camara.
        """
        response = self.client.get('/apirest/comunicaciones/?tipo_camara=Diputados')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)  
        
    def test_comunicacion_codigo_origen(self):
        """
        Prueba que traiga las comunicaciones filtrando por codigo de origen.
        """
        response = self.client.get('/apirest/comunicaciones/?codigo_origen=S')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)

    def test_comunicacion_codigo_exp(self):
        """
        Prueba que traiga las comunicaciones filtrando por codigo de expediente.
        """
        response = self.client.get('/apirest/comunicaciones/?codigo_exp=0114-S-1997')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXP)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        
    def test_comunicacion_codigo_num(self):
        """
        Prueba que traiga las comunicaciones filtrando por codigo de numero.
        """        
        response = self.client.get('/apirest/comunicaciones/?codigo_num=0114')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXP)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO)      
        
    def test_comunicacion_periodo(self):
        """
        Prueba que traiga las comunicaciones filtrando por periodo
        """                  
        response = self.client.get('/apirest/comunicaciones/?periodo=115')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
            
    def test_fecha_desde_y_hasta(self):
        """
        Prueba que traiga las comunicaciones que pertenecen al rango de fecha indicada.
        """
        response = self.client.get('/apirest/comunicaciones/?fechaDesde=2015-01-01&fechaHasta=2015-04-01')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        
    def test_comunicacion_subtipo(self):
        """
        Prueba que traiga todas las comunicaciones de un determinado subtipo.
        """
        response = self.client.get('/apirest/comunicaciones/?subtipo=PASE A DIPUTADOS')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)        
        
    def test_comunicacion_orden(self):
        """
        Prueba que traiga todas las comunicaciones de un determinado orden.
        """
        response = self.client.get('/apirest/comunicaciones/?orden=2')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
    
    #Test con filtros combinados. 
    def test_codigo_anio_y_codigo_num(self):
        """
        Prueba que traiga las comunicaciones por un anio y numero determinado.
        """
        response = self.client.get('/apirest/comunicaciones/?codigo_num=0114&codigo_anio=1997')   
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)       
        
    def test_codigo_anio_y_orden(self):
        """
        Prueba que traiga las comunicaciones por un anio y orden.
        """
        response = self.client.get('/apirest/comunicaciones/?codigo_anio=2002&orden=2')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO_ORDEN)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)     
        
