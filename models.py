from django.db import models

# Create your models here.

class ContactRecord(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=80)
    phone_number = models.BigIntegerField()
