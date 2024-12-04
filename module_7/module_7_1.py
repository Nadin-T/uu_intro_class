class Product():
    """
    Класс для создания продуктов.
    Атрибуты: название продукта, общий вес товара (дробное число), категория товара.
    """
    def __init__(self, name, weight, category):
        """Инициализирует объект класса Продукт."""
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        """Возвращает строковое представление продукта."""
        return f'{self.name.title()}, {self.weight}, {self.category.title()}.'


class Shop():
    """Класс Магазин."""
    __file_name = 'products.txt'

    def get_products(self):
        """Возвращает информацию о продуктах из файла."""
        file = open(self.__file_name, 'r')
        products_info = file.read()
        file.close()
        return products_info

    def add(self, *products):
        """Добавляет уникальные продукты в файл."""
        file = open(self.__file_name, 'a+')
        file.seek(0)
        products_info = self.get_products()
        for product in products:
            product_str = str(product)
            if product_str not in products_info:
                file.write(product_str + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине.')
        file.close()


if __name__ == '__main__':
    s1 = Shop()

    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')
    print(p2)  # __str__

    s1.add(p1, p2, p3)
    print(s1.get_products())