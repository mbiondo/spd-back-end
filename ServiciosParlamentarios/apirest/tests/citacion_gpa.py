# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestCitacionGpa(APITestCase):
     
    #Constantes usadas para realizar la comparacion en los test.
    CODIGO_EXITO = 200 
    CANT_CITACIONES_GPA = 1
    FK_LUGAR = 1
    VISIBILIDAD = 1
    
    def test_citaciones_gpa(self):
        """
        Prueba el servicio para listar las citaciones gpa. 
        """
        response = self.client.get('/apirest/citaciones_gpa/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_CITACIONES_GPA)
         
    def test_citacion_gpa_lugar(self):
        """
        Prueba el servicio para obtener una citacion filtrando por lugar.
        """
        response = self.client.get("/apirest/citaciones_gpa/?lugar=Sala 1")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
#         self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
#            
    def test_citacion_gpa_id(self):
        """
        Prueba el servicio para obtener una citacion por id. 
        """
        response = self.client.get("/apirest/citaciones_gpa/1/")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["visibilidad"], self.VISIBILIDAD)
        
    def test_citacion_gpa_estado(self):
        """
        Prueba el servicio para obtener una citacion filtrando por estado.
        """
        response = self.client.get("/apirest/citaciones_gpa/?estado=convocada")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        
    def test_citacion_gpa_visibilidad(self):
        """
        Prueba el servicio para obtener una citacion filtrando por visibilidad.
        """
        response = self.client.get("/apirest/citaciones_gpa/?visibilidad=1")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        
    def test_citacion_gpa_fecha_desde(self):
        """
        Prueba el servicio para obtener una citacion filtrando por fecha desde.
        """
        response = self.client.get("/apirest/citaciones_gpa/?fecha_desde=2015-04-21")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["count"], self.CANT_CITACIONES_GPA)
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        
    def test_citacion_gpa_fecha_hasta(self):
        """
        Prueba el servicio para obtener una citacion filtrando por fecha hasta.
        """
        response = self.client.get("/apirest/citaciones_gpa/?fecha_hasta=2015-04-23")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["count"], self.CANT_CITACIONES_GPA)
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)

        
    def test_citacion_gpa_fecha_desde_y_hasta(self):
        """
        Prueba el servicio para obtener una citacion filtrando por rango de fecha.
        """
        response = self.client.get("/apirest/citaciones_gpa/?fecha_desde=2015-04-21&fecha_hasta=2015-04-23")
        self.assertEqual(response.status_code, self.CODIGO_EXITO)        
        self.assertEqual(response.data["count"], self.CANT_CITACIONES_GPA)
        self.assertEqual(response.data["results"][0]["fk_lugar"], self.FK_LUGAR)
        self.assertEqual(response.data["results"][0]["visibilidad"], self.VISIBILIDAD)
        