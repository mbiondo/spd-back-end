# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestCitacion(APITestCase):
     
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANT_CITACIONES = 84
    FK_LUGAR = 1 
    VISIBILIDAD = 1
    REUNION_CONJUNTA = "S"
    CANT_CITACIONES_FECHA_DESDE = 32
    CANT_CITACIONES_FECHA_HASTA = 52
    CANT_CITACIONES_FECHA_RANGO = 1
    
    
     
    def test_citaciones(self):
        """
        Prueba el servicio para listar las cuitaciones. 
        """
        response = self.client.get('/apirest/citaciones/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_CITACIONES)
         
    def test_citacion_lugar(self):
        """
        Prueba el servicio para obtener una citacion filtrando por lugar.
        """
        response = self.client.get("/apirest/citaciones/?lugar=Sala 1")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        self.assertEqual(response.data["results"][0]["reunion_conjunta"], self.REUNION_CONJUNTA)
#            
    def test_citacion_id(self):
        """
        Prueba el servicio para obtener una citacion por id. 
        """
        response = self.client.get("/apirest/citaciones/1/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["visibilidad"], self.VISIBILIDAD)
        self.assertEqual(response.data["reunion_conjunta"], self.REUNION_CONJUNTA)
        
    def test_citacion_estado(self):
        """
        Prueba el servicio para obtener una citacion filtrando por estado.
        """
        response = self.client.get("/apirest/citaciones/?estado=convocada")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        self.assertEqual(response.data["results"][0]["reunion_conjunta"], self.REUNION_CONJUNTA)
        
    def test_citacion_visibilidad(self):
        """
        Prueba el servicio para obtener una citacion filtrando por visibilidad.
        """
        response = self.client.get("/apirest/citaciones/?visibilidad=1")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        self.assertEqual(response.data["results"][0]["reunion_conjunta"], self.REUNION_CONJUNTA)
        
    def test_citacion_fecha_desde(self):
        """
        Prueba el servicio para obtener una citacion filtrando por fecha desde.
        """
        response = self.client.get("/apirest/citaciones/?fecha_desde=2015-06-14")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["count"], self.CANT_CITACIONES_FECHA_DESDE)
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        self.assertEqual(response.data["results"][0]["reunion_conjunta"], self.REUNION_CONJUNTA)
        
    def test_citacion_fecha_hasta(self):
        """
        Prueba el servicio para obtener una citacion filtrando por fecha hasta.
        """
        response = self.client.get("/apirest/citaciones/?fecha_hasta=2015-06-14")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["count"], self.CANT_CITACIONES_FECHA_HASTA)
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        self.assertEqual(response.data["results"][0]["reunion_conjunta"], self.REUNION_CONJUNTA)
        
    def test_citacion_fecha_desde_y_hasta(self):
        """
        Prueba el servicio para obtener una citacion filtrando por rango de fecha.
        """
        response = self.client.get("/apirest/citaciones/?fecha_desde=2015-06-13&fecha_hasta=2015-06-14")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["count"], self.CANT_CITACIONES_FECHA_RANGO)
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        self.assertEqual(response.data["results"][0]["reunion_conjunta"], self.REUNION_CONJUNTA)
        
    
              