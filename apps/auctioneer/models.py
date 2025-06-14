from django.db import models

# Create your models here.
class Auctioneer(models.Model):
    name = models.CharField('Nome', max_length=50)
    email = models.EmailField('E-mail', max_length=100, unique=True)
    phone = models.CharField('Telefone', max_length=15, blank=True, null=True, help_text='Formato: (XX) XXXXX-XXXX')

    class Meta:
        verbose_name = 'Leiloeiro'
        verbose_name_plural = 'Leiloeiros'
        ordering =['id']

    def __str__(self):
        return self.name