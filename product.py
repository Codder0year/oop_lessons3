"""Test, 1000 руб. Остаток: 10 шт.
    True
    Test2, 500 руб. Остаток: 20 шт.
    Для класс Product добавить строковое отображение в следующем виде:

    Название продукта, 80 руб. Остаток: 15 шт.

    В предыдущей домашке вы делали геттер для класса Category для вывода списка товаров, теперь каждый продукт имеет реализованное строковое отображение.
     Вы можете вернуться к этому геттеру и оптимизировать его работу, просто преобразовав объект продукта в строку.

    Для класса Category добавить строковое отображение в следующем виде:

    Название категории, количество продуктов: 200 шт.

    Для удобства работы с продуктами реализовать возможность их складывать. Логика сложения должна работать так, чтобы в итоге у вас получалась полная стоимость всех товаров на складе. Например, для товара a с ценой 100 рублей и количеством на складе 10 и товара b с ценой 200 рублей и количеством на складе 2 результатом выполнения операции a + b должно стать значение, полученное из 100 * 10 + 200 * 2 = 1400.
"""


class Product:
    """
    Класс для описания товара в магазине
    """
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_):
        return cls(**dict_)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = value

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'


    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)


class Category:
    """
    Класс для категорий товара
    """
    category_count = 0
    product_count = 0
    name = str
    description = str
    products = list

    def __init__(self, products, name, description):
        self.__products = products
        self.name = name
        self.description = description
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, new_product):
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def __str__(self):
        list_ = []
        for product in self.__products:
            n = product.name
            p = product.price
            q = product.quantity
            list_.append(f'{n}, {p} руб. Остаток: {q} шт.\n')
        return ''.join(list_)




data = [
    {
        "name": "Смартфоны",
        "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        "products": [
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14
            }
        ]
    },
    {
        "name": "Телевизоры",
        "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        "products": [
            {
                "name": "55 QLED 4K",
                "description": "Фоновая подсветка",
                "price": 123000.0,
                "quantity": 7
            }
        ]
    }
]
categories = []
for category in data:
    products = []
    for product in category['products']:
        products.append(Product.new_product(product))
    category['products'] = products
    categories.append(Category(**category))

product_item = Product('Test', 'Test', 1000, 10)
print(product_item)
print(str(product_item) == 'Test, 1000 руб. Остаток: 10 шт.')
product_item_2 = Product('Test2', 'Test2', 500, 20)
print(product_item_2)
print(product_item + product_item_2)



