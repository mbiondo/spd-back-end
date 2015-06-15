# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase

class TestProyecto(APITestCase):
    
    # Constantes para corroborar el resultado de los test
    CANT_PROYECTO = 264474    
    CANT_PROYECTO_ID = 1
    CANT_DICTAMEN_CAMARA = 27493
    CANT_COMISION = 8299
    CANT_COMISION_NOMBRE = 7922
    CANT_FIRMANTES_ID = 264398 
    CANT_TIPO_CAMARA = 175534
    CANT_CODIGO_ORIGEN= 2756
    CANT_PERIODO_132 = 12579
    CANT_CODIGO_ORIGEN= 2756
    CANT_PERIODO_132 = 12579
    CANT_OD_NUMERO = 26
    CANT_OD_ANIO = 3115
    CANT_OD_NUMERO_ANIO = 8    
    CANT_PROYECTO_LEY = 73086
    CANT_PROYECTOS_X_FIRMANTE = 264474
    CANT_PROYECTOS_X_FIRMANTE_NOMBRE = 1352
    CANT_PROYECTOS_CARGO_FIRMANTE = 1093
    CANT_PROYECTOS_CARGO_TIPO_FIRMANTE = 3691
    CANT_PROYECTOS_ORDEN_FIRMANTE = 166509
    CANT_CODIGO_NUM_Y_ANIO = 4
    CANT_RESULTADO_Y_ANIO = 4
    CANT_COMISION_NOMBRE_Y_CODIGO_ANIO = 466
    CANT_CODIGO_ANIO_Y_FIRMANTE = 146 
    CANT_RESULTADO_APROBACION = 647
    
    CODIGO_EXITO = 200
    CODIGO_NUM = '0001'  
    TIPO_CAMARA = "Diputados"
    SUMARIO = "APROBACION."
    CODIGO_ANIO = "1984"
    CODIGO_EXP = "0001-PE-1984"
    FECHA_CADUCIDAD = "1899-12-30"
    CODIGO_ORIGEN = "PE"
    PERIODO = 132
    NUMERO_OD = 1
    ANIO_OD = 2010
    TIPO = "PROYECTO"
    TIPO_PROY_ARCHIVO = "RESOLUCION"
    CODIGO_ANIO_RESUTLADO = "2006"
    CODIGO_ANIO_COMPUESTO  = "2014"
    


    # Test: ATRIBUTOS DE PROYECTOS.
    def test_proyecto(self):
        """
        Prueba servicio de proyectos.  
        """
        response = self.client.get('/apirest/proyectos/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PROYECTO)
        
    def test_proyecto_id(self):
        """
        Prueba el servicio para traer un proyecto por id
        """
        response = self.client.get('/apirest/proyectos/4/')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["codigo_num"], self.CODIGO_NUM)
        
    # Test sobre filtros. 
    def test_proyecto_tipo_ley(self):
        """
        Prueba que traiga los proyectos filtrando por tipo de ley-.
        """
        response = self.client.get('/apirest/proyectos/?tipo_proy=LEY')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PROYECTO_LEY)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        
    
    def test_proyecto_tipo_camara(self):
        """
        Prueba que traiga los proyectos filtrando por tipo de camara.
        """
        response = self.client.get('/apirest/proyectos/?tipo_camara=Diputados')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["sumario"], self.SUMARIO)  
        
    def test_proyecto_codigo_origen(self):
        """
        Prueba que traiga los proyectos filtrando por codigo de origen.
        """
        response = self.client.get('/apirest/proyectos/?codigo_origen=PE')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["sumario"], self.SUMARIO) 

    def test_proyecto_codigo_exp(self):
        """
        Prueba que traiga los proyectos filtrando por codigo de expediente.
        """
        response = self.client.get('/apirest/proyectos/?codigo_exp=0001-PE-1984')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXP)
        self.assertEqual(response.data["results"][0]["sumario"], self.SUMARIO) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO)
        
    def test_proyecto_codigo_num(self):
        """
        Prueba que traiga los proyectos filtrando por codigo de numero.
        """        
        response = self.client.get('/apirest/proyectos/?codigo_num=0001')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["results"][0]["codigo_exp"], self.CODIGO_EXP)
        self.assertEqual(response.data["results"][0]["sumario"], self.SUMARIO) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO)      
        
    def test_proyecto_fecha_caducidad(self):
        """
        Prueba que traiga los proyectos filtrando por fecha de caducidad
        """                  
        response = self.client.get('/apirest/proyectos/?fecha_caducidad=1899-12-30')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][1]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][1]["fecha_caducidad"], self.FECHA_CADUCIDAD) 
        
    def test_proyecto_periodo(self):
        """
        Prueba que traiga los proyectos filtrando por periodo
        """                  
        response = self.client.get('/apirest/proyectos/?periodo=132')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_PERIODO_132)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO) 
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)  
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
            
    def test_fecha_desde_y_hasta(self):
        """
        Prueba que traiga los proyectos que pertenecen al rango de fecha indicada.
        """
        response = self.client.get('/apirest/proyectos/?fechaDesde=2015-01-01&fechaHasta=2015-04-01')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        
    # TEST sobre ordenes del día.        
    def test_proyecto_od_numero(self):
        """
        Prueba que traiga los proyectos filtrando por numero de od
        """  
        response = self.client.get('/apirest/proyectos/?od_numero=1') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_OD_NUMERO)
        self.assertEqual(response.data["results"][0]["periodo"], self.PERIODO)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        
    def test_proyecto_od_anio(self):
        """
        Prueba que traiga los proyectos filtrados por anio de OD.
        """
        response = self.client.get('/apirest/proyectos/?od_anio=2014') 
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_OD_ANIO)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        
    def test_proyecto_od_numero_anio(self):
        """
        Prueba que traiga los proyectos filtrados por numero y anio de OD.
        """
        response = self.client.get('/apirest/proyectos/?od_numero=1&od_anio=2014')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_OD_NUMERO_ANIO)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA) 
        
    #Test sobre resultados.
    def test_proyecto_resultado_nro_ley(self):
        """
        Prueba que traiga los proyectos por numero de ley. 
        """        
        response = self.client.get('/apirest/proyectos/?nro_ley=25413')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA) 
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        
    def test_proyecto_resultado(self):
        """
        Prueba que traiga los proyectos por resultado. 
        """        
        response = self.client.get('/apirest/proyectos/?resultado=ARCHIVO')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_proy"], self.TIPO_PROY_ARCHIVO)
        
    #Test sobre despacho.
    def test_proyecto_dictamen_camara(self):
        """
        Prueba que traiga los proyectos por tipo de camara de despacho
        """
        response = self.client.get('/apirest/proyectos/?dictamen_camara=diputados')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"], self.CANT_DICTAMEN_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA) 
        
    #Test sobre giros-
    def test_proyecto_giros_comision_id(self):
        """
        Prueba que traiga los proyectos por id de comision.
        """
        response = self.client.get('/apirest/proyectos/?giro_comision_id=5')
        self.assertEqual(response.data["count"], self.CANT_COMISION)
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        
    def test_proyecto_giros_comision_nombre(self):    
        """
        Prueba que traiga los proyectos por nombre de comision.
        """
        response = self.client.get('/apirest/proyectos/?giro_comision_nombre=TRANSPORTES')
        self.assertEqual(response.data["count"], self.CANT_COMISION_NOMBRE)
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        
    def test_proyecto_giros_comision_nombre_corto(self):    
        """
        Prueba que traiga los proyectos por nombre corto de comision.
        """
        response = self.client.get('/apirest/proyectos/?giro_comision_nombre_corto=TRANSPORTES')
        self.assertEqual(response.data["count"], self.CANT_COMISION_NOMBRE)
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        
    #Test sobre firmantes.
    def test_firmante_id(self):
        """
        Prueba que traiga los proyectos que fueron firmados por id de firmante.
        """
        response = self.client.get('/apirest/proyectos/?firm_persona_fisica_id=1566')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_PROYECTOS_X_FIRMANTE)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        
    def test_firm_nombre_leg_func(self):
        """
        Prueba que traiga los proyectos que fueron firmados por nombre de firmante.
        """
        response = self.client.get('/apirest/proyectos/?firm_nombre_leg_func=GERARDO RUBEN MORALES')
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_PROYECTOS_X_FIRMANTE_NOMBRE)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        
    def test_firm_cargo(self):
        """
        Prueba que traiga los proyectos que fueron firmados por cargo de firmante
        """
        response = self.client.get('/apirest/proyectos/?firm_cargo=Jefe de Gabinete de Ministros')   
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_PROYECTOS_CARGO_FIRMANTE)   
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)  
        
    def test_firm_cargo_tipo(self):
        """
        Prueba que traiga los proyectos que fueron firmados por tipo de cargo de firmante
        """
        response = self.client.get('/apirest/proyectos/?firm_cargo_tipo=FUNCIONARIO')   
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_PROYECTOS_CARGO_TIPO_FIRMANTE)   
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)                  

    def test_firm_orden(self):
        """
        Prueba que traiga los proyectos que fueron firmados por tipo de cargo de firmante
        """
        response = self.client.get('/apirest/proyectos/?firm_orden=1')   
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_PROYECTOS_ORDEN_FIRMANTE)   
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)
        self.assertEqual(response.data["results"][0]["tipo_camara"], self.TIPO_CAMARA)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)      
          
    #Test con filtros combinados. 
    def test_codigo_anio_y_codigo_num(self):
        """
        Prueba que traiga los proyectos pot un anio y numero determinado.
        """
        response = self.client.get('/apirest/proyectos/?codigo_num=0001&codigo_anio=1984')   
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_CODIGO_NUM_Y_ANIO)   
        self.assertEqual(response.data["results"][0]["codigo_num"], self.CODIGO_NUM)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)       
        
    def test_codigo_anio_y_resultado(self):
        """
        Prueba que traiga los proyectos
        """
        response = self.client.get('/apirest/proyectos/?resultado=RETIRO&codigo_anio=2006')   
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["count"],self.CANT_RESULTADO_Y_ANIO)   
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO_RESUTLADO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)      
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)   
        
    def test_codigo_anio_y_giro_comision_nombre(self):
        """
        Prueba que traiga los proyectos por nombre de comision de un anio determinado.
        """
        response = self.client.get('/apirest/proyectos/?giro_comision_nombre=TRANSPORTES&codigo_anio=2014')
        self.assertEqual(response.data["count"], self.CANT_COMISION_NOMBRE_Y_CODIGO_ANIO)
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_origen"], self.CODIGO_ORIGEN)  
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO_COMPUESTO)
        
    def test_codigo_anio_y_firmante_nombre_leg_func(self):
        """
        Prueba que traiga los proyectos por nombre de comision de un anio determinado.
        """
        response = self.client.get('/apirest/proyectos/?firm_nombre_leg_func=GERARDO RUBEN MORALES&codigo_anio=2014')
        self.assertEqual(response.data["count"], self.CANT_CODIGO_ANIO_Y_FIRMANTE)
        self.assertEqual(response.status_code, self.CODIGO_EXITO)
        self.assertEqual(response.data["results"][0]["tipo"], self.TIPO)
        self.assertEqual(response.data["results"][0]["codigo_anio"], self.CODIGO_ANIO_COMPUESTO)        