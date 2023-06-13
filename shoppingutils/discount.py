new_cart = []

def apply_discount(cart, discount):
    """
    calculo o desconto de todos os itens da lista

    :param cart:
    :param discount:
    :return:
    """
    for i in range(len(cart)):
        preco = cart[i] - (cart[i] * discount)
        new_cart.append(preco)
    return print(new_cart)

