from apirest.utils.constants import Constants

class ApirestRouter(object):
    """
    A router to control all database operations on models in the
    apirest application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read apirest models go to pap_nueva_pruebas.
        """
        if model._meta.app_label == Constants().APIREST:
            return Constants().PAP
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write apirest models go to pap_nueva_pruebas.
        """
        if model._meta.app_label == Constants().APIREST:
            return Constants().PAP
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the apirest app is involved.
        """
        if obj1._meta.app_label == Constants().APIREST or obj2._meta.app_label == Constants().APIREST:
            return True
        return None
     
    def allow_syncdb(self, db, model):
        """
        Make sure the apirest only appears in the 'pap_nueva_pruebas'
        database.
        """
        if db == str(Constants().PAP):
            return model._meta.app_label == Constants().APIREST
        elif model._meta.app_label == Constants().APIREST:
            return False
        return None        
