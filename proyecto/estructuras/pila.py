class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.items:
            return self.items.pop()

    def ver(self):
        return self.items