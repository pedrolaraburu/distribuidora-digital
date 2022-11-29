from django.db import models
from django.urls import reverse_lazy

# Create your models here.

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField('Preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('Estoque atual')
    estoque_minimo = models.PositiveIntegerField('Estoque mínimo', default=0)

    class Meta:
        ordering = ('produto',)
    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('produto:produto_detail', kwargs={'pk' : self.pk})
    def get_add_to_cart_url(self):
        return reverse_lazy('produto:add-carrinho', kwargs={'pk': self.pk})
    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }


class Carrinho(models.Model):
    produtoCarrinho = models.ForeignKey(
        Produto,
        related_name='produtos',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    quantity = models.PositiveIntegerField('quantidade', default=1)


    class Meta:
        ordering = ('-pk',)
        verbose_name = 'carrinho'
        verbose_name_plural = 'carrinhos'

    def __str__(self):
        return f'{self.pk}-{self.produtoCarrinho}'

    def get_subtotal(self):
        return self.price * (self.quantity or 0)
    
    def get_total_item_price(self):
        return self.quantity * self.produtoCarrinho.preco

    def get_remove_from_cart_url(self):
        return reverse_lazy('produto:retirar_produto', kwargs={'pk': self.pk})

