import os

class node():
    def __init__(self, dato):
        self.left = None
        self.rigth = None
        self.datp = dato

class arbol():
    def __init__(self):
        self.root = None

    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left,dato)
            else:
                a.rigth = self.insert(a.rigth, dato)
        return a

    def inoder(sel, a):
        pass
