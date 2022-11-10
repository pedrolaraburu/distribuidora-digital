import os
import django
import string
import timeit
from random import choice, randint, random


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")

django.setup()
from projeto.produto.models import Produto



class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:

    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random() * randint(10, 50),
                estoque=randint(10, 200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    'Guaraná 250ml',
    'Heineken 350ml',
    'Coca-Cola 330ml',
    'Brahma Malzbier 350ml',
    'Brahma Cerveja duplo malte 369ml',
    'Skol beats 269ml',
    'Fanta Laranja 330ml',
    'Fanta Uva 330ml',
    'Guaraná Jesus 250ml',
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)


toc = timeit.default_timer()

print('Tempo:', toc - tic)