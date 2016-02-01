"""Övningar på ADTn unordered list."""

class Node():
    """Implementation av nod för `UnorderedList`.
    """

    def __init__(self, data, next):
        """Initiera noden med attributen `self.data` och `self.next`.
        """
        self.data = data
        self.next = next


class UnorderedList():
    """Implementation av ADTn oordnad lista (unordered list).

    Listans första element har index 0.
    """

    def __init__(self):
        """Initiera den tomma listan.
        """
        self.head = None

    def is_empty(self):
        """Returnerar `True` om listan är tom, annars `False`.
        """
        return self.head is None

    def add(self, item):
        """Lägg till `item` i början av listan.
        """
        self.head = Node(item, self.head)

    def size(self):
        """Returnerar antalet värden i listan.
        """
        current = self.head
        count = 0
        #None evals False
        while current:
            count += 1
            current = current.next

        return count

    def search(self, item):
        """Returnerar `True` om `item` finns i listan, annars `False`.
        """
        current = self.head
        #None evals False
        while current:
            if current.data is item:
                return True
            current = current.next
        return False


        # while current.data is not item:
        #     if current.next is not None:
        #         current = current.next
        #     else:
        #         return False

        # return True

    def remove(self,item):
        """Raderar första förekomsten av `item` från listan.
        """
        #None evals False
        #FÖRSTA ITEMS I LISTAN PÅ LISTOR SOM ÄR STÖRRE ÄN TVÅ GÅR INTE
        try:
            if self.size() > 2: 
                if self.head.data == item:
                    var = self.head.next.next
                    del self.head.next
                    self.head.next = var
                    return
                else:               
                    current = self.head
                    while current:
                        if current.next.data is item:
                            var = current.next.next
                            del current.next
                            current.next = var
                            return
                        current = current.next
            elif self.size() <= 2:
                if self.head == None:
                    raise ValueError 
                elif self.head.data == item:
                    del self.head
                    self.head = None
                    return
                elif self.head.next.data == item:
                    var = self.head.next.next
                    del self.head.next
                    self.head.next = var
                    return
                else:
                    raise ValueError
        except:
            raise ValueError

    def append(self, item):
        """Lägg till `item` i slutet av listan.
        """
        #None evals False
        if self.head == None:
            self.add(item)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(item, None)
        
    def insert(self, item, position=None):
        """Lägg till `item` på index `position`.
        """
        if self.head == None:
            self.add(item)
            return
        try:
            if position <= self.size():
                current = self.head
                #förstår inte varför -1 behövs
                for i in range(position-1):
                    current = current.next
                current.next = Node(item, current.next)
            else:
                raise ValueError
        except:
            raise ValueError

    def index(self, item):
        """Returnerar index i listan för första förekomsten av `item`.
        """
        current = self.head

        for i in range(self.size()):
            if item == current.data:
                return i
            elif current.next != None:
                current = current.next
            else:
                raise ValueError

    def pop(self, position=None):
        """Plockar bort och returnerar värdet på index `position`.

        Om inget värde anges för `position` tolkas det som sista värdet.
        """ 
        #None eval False
        if self.size() >= 3:
            current = self.head
           
            if position != None:
                for i in range(position-1):
                    current = current.next
                
                delins = current.next
                returnval = delins.data
                current.next = current.next.next
                del delins
                return returnval 
            else:
                while current.next.next != None:
                    current = current.next
                returnval = current.next.data
                del current.next
                current.next = None
                return returnval
        elif self.size() == 2:
            if position == None:
                del self.head.next
                self.head.next = None
                return
            else:
                if position == 1:
                    returnval = self.head.next.data
                    del self.head.next
                    self.head.next = None
                    return returnval
                elif position == 0:
                    returnval = self.head.data
                    var = self.head.next
                    del self.head
                    self.head = var
                    return returnval
                else:
                    raise ValueError
        elif self.size() == 1:
            if position == None or position == 0:
                returnval = self.head.data
                del self.head
                self.head = None
                return returnval
            else:
                raise ValueError
        elif self.size() == 0:
            raise ValueError
        else:
            print("FML")






    def list_em(self):
        current = self.head
        #None evals False
        while current:
            print(current.data)
            current = current.next

