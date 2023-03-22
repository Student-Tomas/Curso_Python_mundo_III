# Challenge number 076: create a single tuple that contains a list of products with its respective prices, tabulated and formatted
products_list = ('pencil', 1.25, 'eraser', 2.25, 'note book', 5.5, 'pen', 2, 'backpack', 30.5, 'book', 15, 'uniform', 20)
print("="*40)
print(f'{"PRICE LIST":^40}')
print("="*40)
for pos in range(0, len(products_list)):
    if pos % 2 == 0:
        print(f'{products_list[pos]:.<30}',end=" ")
    else:
        print(f"R$ {products_list[pos]:>5.2f}")

