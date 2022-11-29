from django.contrib import admin

from .models import Produto, Carrinho

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'importado',
        'ncm',
        'preco',
        'estoque',
        'estoque_minimo',
    )
    search_fields=('produto',)
    list_filter=('importado',)


@admin.register(Carrinho)
class ProdutoCarrinho(admin.ModelAdmin):
    list_display = (
        '__str__',
        'quantity',
        'get_total_item_price'
    )
