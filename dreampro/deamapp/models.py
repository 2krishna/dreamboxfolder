from django.db import models

# Create your models here.
class CSVMap(models.Model):

    id_in_doc = models.IntegerField()

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    ip_address = models. GenericIPAddressField()
    app_name=models.CharField(max_length=255,null=True)