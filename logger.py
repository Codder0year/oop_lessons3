"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""


class Logger:
    def __init__(self, filename, mode='a'):
        """
        Класс, который создает объект, который можно использовать
        вместо open(), чтобы автоматически закрывать файл.
        :param filename: имя файла
        :param mode: режим открытия файла (по умолчанию 'a')
        """
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        """
        Метод, который вызывается при входе в блок контекста.
        Он открывает файл и возвращает файловый дескриптор.
        :return: файловый дескриптор
        """
        self.fp = open(self.filename, self.mode)
        return self.fp

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод, который вызывается при выходе из блока контекста.
        Он закрывает файл.
        """
        self.fp.close()

    def __call__(self, message):
        """
        магический метод, который позволяет использовать объект класса Logger как функцию,
        принимающую сообщение и записывающую его в файл.
        :param сообщение, которое нужно записать в файл
        """
        with open(self.filename, 'a') as f:
            f.write(message)
        print(message)

# код для проверки
logger = Logger("log.txt")
logger("This is a test message.")
