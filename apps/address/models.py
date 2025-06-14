from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField('Rua', max_length=100)
    number = models.CharField('Número', max_length=10)
    city = models.CharField('Cidade', max_length=100)
    state = models.CharField('Estado', max_length=100)