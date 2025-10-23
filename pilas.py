class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self.items.pop()

    def ver_tope(self):
        if self.esta_vacia():
            raise IndexError("Pila vacía")
        return self.items[-1]

    def tamano(self):
        return len(self.items)