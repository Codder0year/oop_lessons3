"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:
    def __init__(self, data):
        '''
        конструктор, принимающий список элементов;
        :param data: список
        '''
        self.data = data
        self.index = 0

    def __iter__(self):
        '''
        магический метод, который возвращает итератор;
        :return:  итератор
        '''
        self.index = 0
        return self

    def __next__(self):
        '''
        магический метод, который возвращает следующий элемент последовательности;
        :return: следующий элемент последовательности
        '''
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):
        '''
        магический метод, который позволяет обратиться к элементу списка по индексу.
        :param index: элемент
        :return:
        '''
        return self.data[index]


# код для проверки 
my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i, end="")  # 123

print(f'\n{my_list[1]}')  # 2
