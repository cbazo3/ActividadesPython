class GrafoDirigido:
    def __init__(self):
        self.gdirigido = {}

    def añadir_vertice(self, vertice):
        if vertice in self.gdirigido:
            return "El vértice ya existe en este Grafo"
        self.gdirigido[vertice] = []

    def añadir_arista(self, arista):
        v1 = arista.get_v1()
        v2 = arista.get_v2()
        if v1 not in self.gdirigido:
            raise ValueError(f'Vertex {v1.get_name()} no está añadido en el grafo')
        if v2 not in self.gdirigido:
            raise ValueError(f'Vertex {v2.get_name()} no está añadido en el grafo')
        self.gdirigido[v1].append(v2)

    def esta_vertice_en(self, vertice):
        return vertice in self.gdirigido

    def obtener_vertice(self, nombre_vertice):
        for v in self.gdirigido:
            if nombre_vertice == v.get_name():
                return v
        print(f' El vértice {nombre_vertice} no existe')

    def obtener_vecinos(self, vertice):
        return self.gdirigido[vertice]

    def __str__(self):
        all_aristas = ''
        for v1 in self.gdirigido:
            for v2 in self.gdirigido[v1]:
                all_aristas += v1.get_name() + '---->' + v2.get_name() + '\n'
        return all_aristas


class GrafoUnidireccional(GrafoDirigido):
    def añadir_arista(self, arista):
        GrafoDirigido.añadir_arista(self, arista)
        arista_inversa = Arista(arista.get_v2(), arista.get_v1())
        GrafoDirigido.añadir_arista(self, arista_inversa)


class Arista:
    def __init__(self, origen, destino):
        self.origen = origen
        self.destino = destino

    def get_v1(self):
        return self.origen

    def get_v2(self):
        return self.destino

    def __str__(self):
        return self.origen.get_name() + '---->' + self.destino.get_name()


class Vertice:
    def __init__(self, nombre):
        self.nombre = nombre

    def get_name(self):
        return self.nombre

    def __str__(self):
        return self.nombre


def construir_grafo(grafo):
    g = grafo()
    for v in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'x'):
        g.añadir_vertice(Vertice(v))
    g.añadir_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('a')))
    g.añadir_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('b')))
    g.añadir_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('c')))
    g.añadir_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('d')))
    g.añadir_arista(Arista(g.obtener_vertice('a'), g.obtener_vertice('e')))
    g.añadir_arista(Arista(g.obtener_vertice('a'), g.obtener_vertice('f')))
    g.añadir_arista(Arista(g.obtener_vertice('s'), g.obtener_vertice('g')))
    g.añadir_arista(Arista(g.obtener_vertice('g'), g.obtener_vertice('i')))
    g.añadir_arista(Arista(g.obtener_vertice('f'), g.obtener_vertice('x')))

    return g

G1 = construir_grafo(GrafoDirigido)

print(G1)
