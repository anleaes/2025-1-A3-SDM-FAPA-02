from django.db import models
from auctioneer.models import Auctioneer
# Create your models here.

class Auction(models.Model):
    title = models.CharField('Título', max_length=200)
    description = models.TextField('Descrição')
    address = models.ForeignKey('address.Address', on_delete=models.CASCADE)
    start_date = models.DateTimeField('Data Início')
    end_date = models.DateTimeField('Data Fim')
    auctioneer = models.ForeignKey(Auctioneer, on_delete=models.CASCADE, related_name='auctions')

    class Meta:
        verbose_name = 'Leilão'
        verbose_name_plural = 'Leilões'
        ordering =['id']

    def __str__(self):
        return self.name