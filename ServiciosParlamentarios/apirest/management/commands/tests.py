from django.core.management.base import BaseCommand
import unittest
from apirest.utils.constants import Constants
import inspect
import pkgutil
import apirest.tests

class Command(BaseCommand):
    
    help = 'Testing against existing database'
    suite = unittest.TestSuite()
    
    def load_all_tests(self):
        """
        This method gets all the Tests in apirest.tests automatically by module 
        """
        package = apirest.tests
        prefix = package.__name__ + "."
        
        for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix):
            module = __import__(modname, fromlist="dummy")
            clsmembers = inspect.getmembers(module, inspect.isclass)
            for name, obj in clsmembers:
                if(name.startswith('Test') == True):
                    test = module.__name__ + "." + name
                    self.suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))

    def handle(self, *args, **options):
        Constants().PAP = 'pap_nueva_pruebas_test'
        if len(args) == 0:  #NoArgs -> All tests
            self.load_all_tests()         
        else:               #Only args to be tested
            for test in args:
                self.suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
            
        unittest.TextTestRunner().run(self.suite)
        
        