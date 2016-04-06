"""Övningar på BinarySearchTree (BST).

Ett BST är ett rotat binärt träd där varje nod har en `key` och ett eventuellt värde, `value`. Varje nod i trädet finns två träd,
`left` och `right`. En nods `key` måste vara större än alla noders `key`i det vänstra trädet och mindre än alla noders `key` i det högra trädet.

`Wikipedia <https://en.wikipedia.org/wiki/Binary_search_tree>`_
"""


class BinarySearchTree():
    """Implementation av BinarySearchTree (BST)."""

    def __init__(self, key, value=None):
        """Initierar det tomma trädet."""
        self.key = key
        self.left = None
        self.right = None
        self.value = value

    def insert(self, key, value=None):
        """Lägger till en nod i trädet."""
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
        """Söker efter noden med matchande key.

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
        "tar bort noden som ska tas bort och ersätt den med den nod som har högst värde av dem som har mindre värde än den som ska deletas"

        if key == self.key:
            number_of_children = 0
            if self.left:
                number_of_children += 1
            if self.right:
                number_of_children += 1

            if number_of_children == 0:  
                if parent.left == self:
                    parent.left = None
                else:
                    parent.right = None

            elif number_of_children == 1: 
                if self.left is not None:  
                    new_node = self.left
                else:                     
                    new_node = self.right

                if parent.left == self:
                    parent.left = new_node
                else:
                    parent.right = new_node

            elif number_of_children == 2:
                # 1. find node with
                    # a. highest key to the left of self or
                    # b. lowest key to the right of self
                # 2. set pointer of parent.left or parent.right to node

                # follow self.left of self.right to find right replacement-node
                successor = self.right
                successor_parent = self
                while successor.left:
                    successor_parent = successor
                    successor = successor.left

                if parent:
                    # Modify pointers so current will fit in it's new spot
                    successor.left = self.left
                    successor.right = self.right

                    # Update parent's pointer
                    if parent.left == self:
                        parent.left = successor
                    else:
                        parent.right = successor

                else:
                    self.key = successor.key
                    self.value = successor.value

                # Delete old position
                if successor_parent.left == successor:
                    successor_parent.left = None
                else:
                    successor_parent.right = None

            return True  # Hopefully a success
        else:
            print("FML")

    def traverse(self):
        """En in-order traversering av trädets noder.

        Implementerad som en generator.
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