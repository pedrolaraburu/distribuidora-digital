from django.urls import path
from projeto.produto import views as v

app_name = 'produto'

urlpatterns = [
    path('', v.produto_list, name='produto_list'),
    path('<int:pk>/', v.produto_detail, name='produto_detail'),
    path('add/', v.ProdutoCreate.as_view(), name='produto_add'),
    path('<int:pk>/edit', v.ProdutoUpdate.as_view(), name='produto_edit'),
    path('<int:pk>/delete', v.ProdutoDelete.as_view(), name='produto_delete'),
    path('<int:pk>/json/', v.produto_json, name='produto_json'),
    path('loja/', v.produto_loja, name='produto_loja'),
    path('carrinho/', v.produto_carrinho, name='produto_carrinho'),
    path('carrinho/add-carrinho/<int:pk>', v.adicionar_carrinho, name='add-carrinho'),
    path('carrinho/retirar-produto/<int:pk>', v.retirar_produto, name='retirar_produto'),
]