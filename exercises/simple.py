"""Övningar på de enklare ADTerna."""

from exceptions import EmptyStack, EmptyQueue


class Stack():
    """Implementation av ADTn stack.
    """

    def __init__(self):
        """Initierar en tom stack.
        """
        self.data = list()

    def push(self, item):
        """Lägg till `item` överst på stacken.
        """
        self.data.append(item)

    def pop(self):
        """Plockar bort och returnerar översta värdet på stacken.
        """
        self.data.pop(-1)
        #emptystackexception
    def peek(self):
        """Returnerar översta värdet på stacken.
        """
        try:
            return self.data[-1]
        except:
            raise EmptyStack

    def is_empty(self):
        """Returnerar `True` om stacken är tom, annars `False`.
        """
        return len(self.data) == 0

    def size(self):
        """Returnerar antalet värden på stacken.
        """
        return len(self.data)


class Queue():
    """Implementation av ADTn kö (queue).
    """

    def __init__(self):
        """Initierar en tom kö.
        """
        self.queue = list()

    def enqueue(self, item):
        """Lägger till `ìtem` i slutuet på kön.
        """
        self.queue.append(item)

    def dequeue(self):
        """Plockar bort det första värdet i kön och returnerar det.
        """
        try:
            self.queue.pop(0)
        except:
            raise EmptyQueue

    def is_empty(self):
        """Returnerar `True` om kön är tom, annars `False`.
        """
        return  len(self.queue) == 0
        

    def size(self):
        """Returnerar antalet värden i kön.
        """
        return len(self.queue)
