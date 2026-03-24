print("\n 1. Выбор заказов")

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

print("\n Функция через List_Comprehension")
def get_expensive_products(any_orders_list):
    return sorted([order["product"] for order in any_orders_list if order["price"] > 500])
print (get_expensive_products(orders))


print("\n Функция через цикл For")

def get_expensive_products2(orders_list):
    names = []
    for order in orders_list:
        if order["price"] > 500:
            names.append(order["product"])
    return sorted(names)

print(get_expensive_products2(orders))

print("\n Функция через Lambda")
filtered = filter(lambda order: order["price"] > 500, orders)
names = map(lambda order: order["product"], filtered)
result = sorted(list(names))
print(result)

print("\n 2. Статистика продаж")
sales = [
    ("Laptop", 5, 1200),
    ("Mouse", 50, 20),
    ("Keyboard", 30, 50),
    ("Monitor", 10, 300),
    ("Chair", 20, 800)
]

def get_sales_stats(sales_data):
    bablo = {item: qty * price for item, qty, price in sales_data}
    return dict(sorted(bablo.items(), key=lambda x: x[1], reverse=True))

print(get_sales_stats(sales))





