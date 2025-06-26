from django.db import models
from bidder.models import Bidder
from item.models import Item
from auction.models import Auction

# Create your models here.
class Bid(models.Model):
    amount = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    date_time = models.DateTimeField('Data do Lance', auto_now_add=True) 
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='bids',  null=True, blank=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='bids',  null=True, blank=True)
    class Meta:
        verbose_name = 'Lance'
        verbose_name_plural = 'Lances'
        ordering =['id']

    def __str__(self):
        return self.name