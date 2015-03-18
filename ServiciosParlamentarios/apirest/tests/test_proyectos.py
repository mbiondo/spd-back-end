# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestProyectos(APITestCase):
    
    CANTIDAD_DE_PROYECTOS = 260703
    CODIGOEXP = "0001-PE-1985" 
    TITULO = "ENRIQUECIMIENTO PATRIMONIAL POR TRANSMISION GRATUITA; IMPUESTO ESTABLECIDO CON CARACTER DE EMERGENCIA."
    VOCES = "IMPUESTOS TASAS CONTRIBUCIONES"
    PERIODO = 103
    
    # Datos exclusivos para la prueba de ordering
    CODIGOEXP_PRIMER_PROYECTO = "0001-D-1984   "
    CODIGOEXP_SEGUNDO_PROYECTO = "0001-D-1986   " 
    CODIGOEXP_TERCER_PROYECTO = "0001-D-1990   "
    CODIGOEXP_CUARTO_PROYECTO = "0001-D-1991   "
    
    def test_get_proyectos(self):
        """
        Prueba que se obtengan todos los proyectos.
        """
        response = self.client.get('/apirest/proyectos/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["count"], self.CANTIDAD_DE_PROYECTOS)
        
    def test_get_proyecto_filter(self):
        """
        Prueba que se obtenga un proyecto por id.
        """
        response = self.client.get('/apirest/proyectos/?codigoexp=0001-PE-1985')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        self.assertEqual(response.data["results"][0]["titulo"], self.TITULO)
        self.assertEqual(response.data["results"][0]["voces"], self.VOCES)
        
    def test_get_proyecto_search(self):
        """
        Prueba que se obtengan los proyecto segun el patron de la busqueda.  
        """  
        response = self.client.get('/apirest/proyectos/?search=tasas')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        self.assertEqual(response.data["results"][0]["titulo"], self.TITULO)
        self.assertEqual(response.data["results"][0]["voces"], self.VOCES)
        
    def test_get_proyecto_ordering(self):
        """
        Prueba que se obtengan los proyecto segun un orden dado.  
        """ 
        response = self.client.get('/apirest/proyectos/?ordering=codigoexp')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data["results"][0]["codigoexp"], self.CODIGOEXP_PRIMER_PROYECTO)
        self.assertEqual(response.data["results"][1]["codigoexp"], self.CODIGOEXP_SEGUNDO_PROYECTO)
        self.assertEqual(response.data["results"][2]["codigoexp"], self.CODIGOEXP_TERCER_PROYECTO)
        self.assertEqual(response.data["results"][3]["codigoexp"], self.CODIGOEXP_CUARTO_PROYECTO)

