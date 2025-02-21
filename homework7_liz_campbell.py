pizza_orders = ['sausage', 'supreme', 'mexican', 'cheese']
finished_pizzas = []

while pizza_orders:
    pizza = pizza_orders.pop()

    print(f"Your pizza pie is finished!")
    finished_pizzas.append(pizza)

print('\n')
for finished_pizza in finished_pizzas:
    print(f'The pizza {finished_pizza.title()} was made')