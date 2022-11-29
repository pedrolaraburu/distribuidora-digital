from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from .forms import ProdutoForm

from django.contrib import messages

from .models import Produto, Carrinho


# Create your views here.

def produto_list(request):
    template_name='produto_list.html'
    objects = Produto.objects.all()
    context={'object_list': objects}
    return render(request, template_name, context)

def produto_loja(request):
    template_name = 'produto_loja.html'
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request,  template_name, context)

def produto_detail(request, pk):
    template_name='produto_detail.html'
    obj = Produto.objects.get(pk=pk)
    context={'object': obj}
    return render(request, template_name, context)

def produto_add(request):
    template_name = 'produto_form.html'
    return render(request, template_name)

def produto_carrinho(request):
    template_name = 'produto_carrinho.html'
    objects = Carrinho.objects.all()
    context = {'object_list': objects}
    return render(request, template_name, context)

class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoDelete(DeleteView):
    model = Produto
    template_name = 'produto_delete.html'
    success_url = reverse_lazy('produto:produto_list')

def produto_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})

def adicionar_carrinho(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    produto.save()
    pedido = Carrinho.objects.get_or_create(
        produtoCarrinho=produto,
        quantity=1
    )
    messages.info(request, "This item quantity was updated.")
    return redirect("produto:produto_loja")

def retirar_produto(request, pk):
    itemCarrinho = get_object_or_404(Carrinho, pk=pk)
    itemCarrinho.delete()
    messages.info(request, "This item was deleted from the database.")
    return redirect("produto:produto_carrinho")