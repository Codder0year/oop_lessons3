"""
Напишите класс MyList, представляющий собой список, имеющий следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __repr__(self): магический метод, возвращающий строковое представление списка,
которое можно использовать для создания нового объекта класса MyList;
- __str__(self): магический метод, возвращающий строковое представление списка;
- __len__(self): магический метод, возвращающий длину списка;
- __add__(self, other): магический метод, который позволяет складывать списки и возвращать новый список.
"""


class MyList:
    def __init__(self, data):
        self.data = data


    def __repr__(self):
        return f'{self.__class__.__name__}("{self.data}")'


    def __str__(self):
        return f'{self.data}'


    def __len__(self):
        return len(self.data)


    def __add__(self, other):
        return self.data + other.data

# код для проверки 
my_list1 = MyList([1, 2, 3])
print(repr(my_list1))  # MyList([1, 2, 3])
print(str(my_list1))  # [1, 2, 3]
print(len(my_list1))  # 3

my_list2 = MyList([4, 5, 6])
my_list3 = my_list1 + my_list2
print(my_list3)  # [1, 2, 3, 4, 5, 6]


# 膩I嶮薤篝爰曷樔黎㌢´　｀ⅷ
# 艇艀裲f睚鳫巓襴骸　　　　贒憊
# 殪幢緻I翰儂樔黎夢'”　,ｨ傾
# 盥皋袍i耘蚌紕偸′　　　 雫寬I
# 悗f篝嚠篩i縒縡齢　　 　 Ⅷ辨f
# 輯駲f迯瓲i軌帶′　　　　　`守I厖孩
# 幢儂儼巓襴緲′　 　 　 　 　`守枢i磬廛
# 嚠篩I縒縡夢'´　　　 　 　　 　 　 `守峽f
# 蚌紕襴緲′　　　　+REP　　　　　‘守畝
# f瓲軌揄′　　　　　　　　　　　　,g