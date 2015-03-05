# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase
import json

class TestCargo(APITestCase):
    
    DESCRIPCION = 'Diputado'

    def test_get_cargo(self):
        """
        Prueba que se pueda obtener el primer cargo (Diputado).
        """
        response = self.client.get('/apirest/cargos/1/')
        self.assertEqual(response.data, {'cargo_id': 1, 'descripcion': self.DESCRIPCION})
        
    def test_get_cargos(self):
        """
        Prueba que se puedan obtener todos los cargos (Diputado).
        """
        desc = 'descripcion'
        
        response = self.client.get('/apirest/cargos/?page_size=100', content_type='application/json')        
        
        json_response = json.dumps(response.data, ensure_ascii=False, encoding='utf-8')
        
        d = json.loads(json_response)

        self.assertEqual(d["count"],39)
        self.assertEqual(unicode(d['results'][0][desc]), 'Diputado')
        self.assertEqual(unicode(d['results'][1][desc]), 'Jefe de Gabinete de Ministros')
        self.assertEqual(unicode(d['results'][2][desc]), 'Ministro de Agricultura, Ganaderia y Pesca')
        self.assertEqual(unicode(d['results'][3][desc]), str('Ministro de Ciencia, Tecnología e Innovación Productiva\r\n').decode('utf-8'))
        self.assertEqual(unicode(d['results'][4][desc]), 'Ministro de Cultura')
        self.assertEqual(unicode(d['results'][5][desc]), 'Ministro de Defensa')
        self.assertEqual(unicode(d['results'][6][desc]), str('Ministro de Desarrollo Social y Coordinación').decode('utf-8'))
        self.assertEqual(unicode(d['results'][7][desc]), 'Ministro de Desarrollo Social y Medio Ambiente')
        self.assertEqual(unicode(d['results'][8][desc]), str('Ministro de Economía').decode('utf-8'))
        self.assertEqual(unicode(d['results'][9][desc]), str('Ministro de Economía y Finanzas Públicas').decode('utf-8'))
        self.assertEqual(unicode(d['results'][10][desc]), str('Ministro de Economía y Producción').decode('utf-8'))
        self.assertEqual(unicode(d['results'][11][desc]), str('Ministro de Educación').decode('utf-8'))
        self.assertEqual(unicode(d['results'][12][desc]), str('Ministro de Educación y Cultura').decode('utf-8'))
        self.assertEqual(unicode(d['results'][13][desc]), 'Ministro de Industria')
        self.assertEqual(unicode(d['results'][14][desc]), 'Ministro de Industria y Turismo')
        self.assertEqual(unicode(d['results'][15][desc]), 'Ministro de Infraestructura y Vivienda')
        self.assertEqual(unicode(d['results'][16][desc]), 'Ministro de Interior')
        self.assertEqual(unicode(d['results'][17][desc]), 'Ministro de Justicia')
        self.assertEqual(unicode(d['results'][18][desc]), 'Ministro de Justicia, Seguridad y Derechos Humanos')
        self.assertEqual(unicode(d['results'][19][desc]), 'Ministro de Justicia y Derecho Humanos')
        self.assertEqual(unicode(d['results'][20][desc]), 'Ministro de Justicia y Derechos Humanos')
        self.assertEqual(unicode(d['results'][21][desc]), str('Ministro de la Producción').decode('utf-8'))
        self.assertEqual(unicode(d['results'][22][desc]), 'Ministro del Interior')
        self.assertEqual(unicode(d['results'][23][desc]), str('Ministro de Planificación Federal, Inversión Pública y Serv.').decode('utf-8'))
        self.assertEqual(unicode(d['results'][24][desc]), 'Ministro de Relaciones Exteriores, Comercio Inter. y Culto')
        self.assertEqual(unicode(d['results'][25][desc]), 'Ministro de Relaciones Exteriores y Culto')
        self.assertEqual(unicode(d['results'][26][desc]), 'Ministro de Salud')
        self.assertEqual(unicode(d['results'][27][desc]), str('Ministro de Salud y Acción Social').decode('utf-8'))
        self.assertEqual(unicode(d['results'][28][desc]), 'Ministro de Seguridad')
        self.assertEqual(unicode(d['results'][29][desc]), 'Ministro de Seguridad Social')
        self.assertEqual(unicode(d['results'][30][desc]), 'Ministro de Trabajo')
        self.assertEqual(unicode(d['results'][31][desc]), str('Ministro de Trabajo, Empleo y Formación de Recursos Humanos').decode('utf-8'))
        self.assertEqual(unicode(d['results'][32][desc]), 'Ministro de Trabajo, Empleo y Seguridad Social')
        self.assertEqual(unicode(d['results'][33][desc]), 'Ministro de Turismo')
        self.assertEqual(unicode(d['results'][34][desc]), 'Ministro de Turismo, Cultura y Deportes') 
        self.assertEqual(unicode(d['results'][35][desc]), str('Presidente de la Nación').decode('utf-8'))
        self.assertEqual(unicode(d['results'][36][desc]), 'Secretario General de la Presidencia')
        self.assertEqual(unicode(d['results'][37][desc]), 'Senador')
        self.assertEqual(unicode(d['results'][38][desc]), str('Vicepresidente de la Nación').decode('utf-8'))
        
        