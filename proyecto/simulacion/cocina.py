import threading
import random
import time

class Cocina(threading.Thread):

    def __init__(self, cola, pila):
        threading.Thread.__init__(self)

        self.cola = cola
        self.pila = pila
        self.pedido_actual = None
        self.running = True

    def run(self):

        while self.running:

            if not self.cola.esta_vacia():

                self.pedido_actual = self.cola.desencolar()

                tiempo = random.randint(3, 8)

                time.sleep(tiempo)

                self.pila.apilar(self.pedido_actual)

                self.pedido_actual = None

            time.sleep(1)