class CheckerRouter:

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app2':
            return 'app2db'
        elif model._meta.app_label == 'app3':
            return 'app3db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app2':
            return 'app2db'
        elif model._meta.app_label == 'app3':
            return 'app3db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'app2' or obj2._meta.app_label == 'app2':
            return True
        elif 'app2' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        elif obj1._meta.app_label == 'app3' or obj2._meta.app_label == 'app3':
            return True
        elif 'app3' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app2':
            return db == 'app2db'
        elif app_label == 'app3':
            return db == 'app3db'
        return None