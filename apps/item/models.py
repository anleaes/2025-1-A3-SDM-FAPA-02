from django.db import models
from category.models import Category


# Create your models here.
class Item(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    starting_value = models.DecimalField('Valor inicial',  decimal_places=2,  default=0.00, max_digits=10)
    final_value = models.DecimalField('Valor final', decimal_places=2, default=0.00, max_digits=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering =['id']

    def __str__(self):
        return self.name
