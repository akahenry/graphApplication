class v_queue: # vertices priority queue - a fila de prioridade de vértices, usada na árvore geradora mínima
    def __init__(self):
        self.list = []
    def __iter__(self): # necessário para usar a classe em loops for (for i in v_queue)
        return iter(self.list)
    def __getitem__(self, key): # necessário para acessar um item indexado na fila (v_queue[i])
        return self.list[key]
    def __setitem__(self, key, value): # necessário para modificar um item indexado na fila (v_queue[i] = x)
        self.list[key] = value
    def insert(self, v): # inserir
        self.list.append(v)
    def pop_min(self): # extrair mínimo
        self.sort()
        min = self.list[0]
        del self.list[0]
        return min
    def is_empty(self): # teste de vacuidade
        return self.list == []
    def is_in(self, v): # teste de pertinência
        return v in self.list
    def sort(self): # reorganizar
        def v_key(v):
            return v.key
        self.list.sort(key=v_key)
    def find_from_id(self, id): # retorna um nodo, dado seu número (index)
        for i in self.list:
            if(i.id == id):
                return i

class vertex: # vértice - usados para montar a árvore geradora mínima e a lista de prioridade
    def __init__(self, id):
        self.pred = None
        self.key = 201 # Como a maior distância entre vértices é 200, 201 é "infinito"
        self.id = id

class adjacency_matrix: # matriz de adjacência - usada para ler as entradas e ser processada na árvore geradora mínima
    def __init__(self, size):
        self.size = size
        self.matrix = []
        self.limited = [] # lista de dispositivos limitados
    def __iter__(self): # necessário para usar a classe em loops for (for i in adjacency_matrix)
        return iter(self.matrix)
    def __getitem__(self, key): # necessário para acessar um item indexado na matriz
        return self.matrix[key]
    def append_line(self, line): # adiciona um nodo à matriz de adjacência (linha nova)
        self.matrix.append([int(x) for x in line.split()])
    def set_limited_devices(self, line): # guarda quais dos nodos são "limitados"
        self.limited = [int(x)-1 for x in line.split()] # menos 1 pois os indices da matriz são de 0 a D-1

class mn_tree: # minimum spanning tree - a arvore geradora mínima em si

    def __init__(self, matrix): # é inicializado com uma matriz de adjacência
        self.matrix = matrix # matriz de adjacência
        self.V = v_queue() # lista de vértices - V(G)
        for i in range(matrix.size): # insere todos os vértices na lista de vértices
            self.V.insert(vertex(i))

    def prim(self): # gera a árvore geradora mínima usando o algoritmo de prim
        q = v_queue() # seja q uma fila vazia
        self.V[0].key = 0 # escolhe o primeiro vértice da fila para ser a raíz
        for i in self.V: # insere todos os vértices em q
            q.insert(i)
        while not q.is_empty():
            u = q.pop_min()
            if(u.id in self.matrix.limited and u.key != 0): # se for limitado, não "faz filhos", mas pode ser filho de um nodo.
                continue                                    # a não ser que seja a raíz, nesse caso, faz um filho apenas.
            for v in self.adjacents(u):
                if(q.is_in(v) and self.f(u,v) < v.key):
                    v.pred = u
                    v.key = self.f(u,v)
                    q.sort()
                    if(u.key == 0 and u.id in self.matrix.limited): # se for limitado e a raíz, só "faz" um filho
                        break

    def adjacents(self, v): # retorna os nodos adjacentes a v
        return [self.V.find_from_id(i) for i in range(len(self.matrix[v.id])) if self.matrix[v.id][i] != 0]

    def f(self, u, v): # retorna o valor da aresta que conecta u com v
        return self.matrix[u.id][v.id]

    def total_cable_needed(self): # retorna a quantidade de cabo necessária
        sum = 0
        for i in self.V:
            sum += i.key
        return sum


campuses_values = [] # lista que guarda os valores para printar de uma vez só no final

N = int(input())
for i in range(N): # para cada campus
    D = int(input())
    am = adjacency_matrix(D)
    for j in range(D): # para cada dispositivo, lê uma linha de adjacencia
        am.append_line(input())
    L = int(input())
    if(L != 0): # se não tiver dispositivos limitados, não recebe-os
        am.set_limited_devices(input())

    minimum_spanning_tree = mn_tree(am) # faz a matriz de adjacência
    minimum_spanning_tree.prim() # executa o algoritmo, gerando a árvore geradora mínima
    campuses_values.append(minimum_spanning_tree.total_cable_needed())

for i in range(len(campuses_values)):
    print("Campus " + str(i+1) + ": " + str(campuses_values[i]))
