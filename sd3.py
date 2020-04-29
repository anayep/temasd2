class noduri(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.h = 1



class avltree(object):

    def insert(self, root, key):

        # parcurgem ca la binary search tree
        if not root:           #daca nu mai avem radacina,key devine radacina
            return noduri(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)    #daca key este mai mica decat radacina facem insertia la stanga
        else:
            root.right = self.insert(root.right, key)  #daca key este mai mare facem insertia la dreapta


        root.h = 1 + max(self.geth(root.left),
                              self.geth(root.right))    #height se incrementeaza cu maximul dintre height de la stanga si height de la dreapta


        bal = self.getbal(root)    #aflam balance factor-ul


        # cazul left left
        if bal > 1 and key < root.left.val:
            return self.rightRotate(root)

            # cazul right right
        if bal < -1 and key > root.right.val:
            return self.leftRotate(root)

            # cazul left right
        if bal > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            #cazul right left
        if bal < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, a):

        b = a.right
        tree2 = b.left
        b.left = a
        a.right = tree2

        # acutalizam height
        a.h = 1 + max(self.geth(a.left),self.geth(a.right))
        b.h = 1 + max(self.geth(b.left),self.geth(b.right))

        # returnam noua radacina
        return b

    def rightRotate(self, a):

        b = a.left
        tree3 = b.right
        b.right = a
        a.left = tree3
        a.h = 1 + max(self.geth(a.left),self.geth(a.right))
        b.h = 1 + max(self.geth(b.left),self.geth(b.right))


        return b

    def geth(self, root):    #returnam inaltimea
        if not root:
            return 0

        return root.h

    def getbal(self, root):   #returnam balance factor-ul
        if not root:
            return 0

        return self.geth(root.left) - self.geth(root.right)

    def afisare(self, root):    #afisare

        if not root:
            return

        print(root.val)
        self.afisare(root.left)
        self.afisare(root.right)


tree = avltree()

root = tree.insert(None, 4)
root = tree.insert(root, 2)
root = tree.insert(root, 3)
root = tree.insert(root, 7)
root = tree.insert(root, 10)
root = tree.insert(root, 9)

tree.afisare(root)
