"""Övningar på BinarySearchTree (BST).

Ett BST är ett rotat binärt träd där varje nod har en `key` och ett
eventuellt värde, `value`. Varje nod i trädet finns två träd,
`left` och `right`. En nods `key` måste vara större än alla noders `key`
i det vänstra trädet och mindre än alla noders `key` i det högra trädet.

Utseendet hos ett BST beror i väldigt hög grad på i vilken ordning noderna
lagts till. I värsta fall degenererar de fullständigt.

`Wikipedia <https://en.wikipedia.org/wiki/Binary_search_tree>`_
"""


class BinarySearchTree():
    """Implementation av BinarySearchTree (BST)."""

    def __init__(self, key, value=None):
        """Initiera det tomma trädet."""
        self.key = key
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key, value=None):
        """Lägg till en nod i trädet."""
        current = self
        while True:
            if key > current.key:
                if current.right == None:
                    current.right = BinarySearchTree(key, value)
                    return
                else:
                    current = current.right
            else:
                if current.left == None:
                    current.left = BinarySearchTree(key, value)
                    return
                else:
                    current = current.left


    def lookup(self, key):
        """Sök efter noden med matchande key.

        Returnerar matchande noden eller None.
        """
        current = self
        while True:
            if key == current.key:
                return current
            else:
                try:
                    if key > current.key:
                        current = current.right
                    else:
                        current = current.left
                except:
                    raise AttributeError

    def delete(self, key):
        """Radera noden med matchande key."""
        def replacement(ins):
            ins = ins.right
            while ins.left != None:
                ins = ins.left
            return ins

        def FindParent(self, key):
            current = self
            while True:
                if key == current.left:
                    direction = "left"
                    return current, direction

                elif key == current.right:
                    direction = "right"
                    return current, direction
                else:
                    if key > current.key:
                        current = current.right
                    elif key <= current.key:
                        current = current.left
                    else:
                        raise AttributeError
                                   
        replacer = replacement(self)
        
        parent, direction = FindParent(self, key)      
        
        if direction == "left":
            mem_right = parent.left.right
            mem_left = parent.left.left
            parent.left = replacer.left
            parent.left.right = mem_right
            parent.left.left = mem_left
            replacer.left = None
            #objektet som låg på replacer.left försvinner?
        elif direction == "right":
            mem_right = parent.right.right
            mem_left = parent.right.left
            parent.right = replacer.left
            parent.right.right = mem_right
            parent.right.left = mem_left
            replacer.left = None
        else:
            print("FML")

    def traverse(self):
        """En in-order traversering av trädets noder.

        Implementera som en generator.
        """

        if not self.left is None:
            for value in self.left.traverse():
                yield value
                #print("left")

        yield self.key
        #print("key")

        if not self.right is None:
            for value in self.right.traverse():
                yield value
                #print("right")

    def __str__(self):
        """Utskrift av trädets alla noder (in-order)."""
        # Använd traverse...
        return ', '.join([str(x) for x in self.traverse()])

def SetupForTest(ins):
    ints = [150, 50, 140, 40, 145, 160, 155, 157, 153]
    for i in ints:
        ins.insert(i)
    print("accomplished")
    return ins
