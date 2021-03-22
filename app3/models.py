from django.db import models

# Create your models here.



class App3Data(models.Model):
    item=models.CharField(max_length=64)

    def __str__(self):
        return self.item

    class Meta:
        # app_label helps django to recognize your db
        app_label = 'app3'
