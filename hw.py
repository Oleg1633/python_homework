#Задача 1.
#Вводится количество и стоимость товара.
#Посчитать сумму за товар.
quantity= input ("введите количество товара")
cost= input ("введите стоимость товара")

quantity_of_goods=int(quantity)
cost_of_goods=int(cost)
goods_cost=quantity_of_goods*cost_of_goods

print("Сумма за товар", goods_cost, "₽")

