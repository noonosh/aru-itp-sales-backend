from django.db import models

# Create your models here.


class Car(models.Model):

    id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=50)
    available_from = models.DateField()
    manufacturer = models.CharField(max_length=50)
    description = models.TextField(max_length=255, null=True)

    def __str__(self):
        return str(self.model_name)
