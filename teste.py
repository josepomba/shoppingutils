from shoppingutils import *

produtos = {'peras': {'quantidades': 20, 'preco': 5},
            'macas': {'quantidades': 40, 'preco': 4},
            'ameixas': {'quantidades': 60, 'preco': 6}
           }

print(produtos.get("peras"))
print(produtos["peras"]["preco"])
#lista = [preco for preco in produtos["peras"]["preco"]]

lista = [5,10,15]

print(calculate_total_price(lista))
apply_discount(lista, 0.5)
