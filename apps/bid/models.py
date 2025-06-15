from django.db import models
from bidder.models import Bidder
from item.models import Item

# Create your models here.
class Bid(models.Model):
    name = models.CharField('Nome', max_length=50)
    amount = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    date_time = models.DateTimeField('Data do Lance', auto_now_add=True) 
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bids')

    class Meta:
        verbose_name = 'Lance'
        verbose_name_plural = 'Lances'
        ordering =['id']

    def __str__(self):
        return self.name