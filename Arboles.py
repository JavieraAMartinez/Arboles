class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        else:
            pass

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierda)
        else:
            return self._buscar_recursivo(valor, nodo_actual.derecha)

    def imprimir_inorden(self):
        self._imprimir_inorden_recursivo(self.raiz)

    def _imprimir_inorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self._imprimir_inorden_recursivo(nodo_actual.izquierda)
            print(nodo_actual.valor, end=' ')
            self._imprimir_inorden_recursivo(nodo_actual.derecha)

arbol = Arbol()
valores = [50, 30, 70, 20, 40, 60, 80]
for valor in valores:
    arbol.insertar(valor)

print("Recorrido Inorden:")
arbol.imprimir_inorden()

print("\n¿El valor 40 está en el árbol?", arbol.buscar(40))
print("¿El valor 90 está en el árbol?", arbol.buscar(90))

