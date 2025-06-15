from django.db import models
from bidder.models import Bidder
from auction.models import Auction
from item.models import Item
# Create your models here.

class Payment(models.Model):
    amount_paid = models.CharField('Valor', max_length=50)
    bidder = models.ForeignKey(Bidder, on_delete=models.CASCADE)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering =['id']

    def __str__(self):
        return f"Pagamento - {self.item.name} ({self.auction.title}) - R$ {self.amount_paid}"