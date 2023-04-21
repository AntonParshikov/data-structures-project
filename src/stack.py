class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        module_name = "__main__"
        class_name = self.__class__.__name__
        return f"<{module_name}.{class_name} object at {hex(id(all))}>"


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        pass

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        pass

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        pass
