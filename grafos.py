def organizar(elemento):
    return arvore[elemento][1]

infinite = 527

roteadores = [
    [0, 9, 7, 1, 2, 8, 1, 5],
    [9, 0, 13, 3, 2, 10, 1, 19],
    [7, 13, 0, 4, 5, 6, 7, 18],
    [1, 3, 4, 0, 60, 61, 63, 5],
    [2, 2, 5, 60, 0, 11, 12, 13],
    [8, 10, 6, 61, 11, 0, 5, 6],
    [1, 1, 7, 63, 12, 5, 0, 5],
    [5, 19, 18, 5, 13, 6, 5, 0]
    ]

roteadores_list = [0, 1, 2, 3, 4]
protoroteadores_list = [5, 6, 7]

arvore = [
    [None,0],
    [None,0],
    [None,0],
    [None,0],
    [None,0],
    [None,0],
    [None,0],
    [None,0]
    ]
   
for roteador in range(len(roteadores)):
    arvore[roteador][0] = None
    arvore[roteador][1] = infinite

raiz = 0
Q = []
arvore[raiz][1] = 0
for roteador in range(len(roteadores_list)):
    Q.append(roteadores_list[roteador])
while len(Q) > 0:
    base = Q[0]
    del Q[0]
    for roteador in range(len(roteadores)):
        if roteador in Q and roteadores[base][roteadores_list[roteador]] < arvore[roteadores_list[roteador]][1]:
            arvore[roteadores_list[roteador]][0] = base
            arvore[roteadores_list[roteador]][1] = roteadores[base][roteadores_list[roteador]]
            Q.sort(key=organizar)
    print(arvore)

for base in range(len(protoroteadores_list)):
    for roteador in range(len(roteadores_list)):
        if roteadores[protoroteadores_list[base]][roteadores_list[roteador]] < arvore[protoroteadores_list[base]][1]:
            arvore[protoroteadores_list[base]][0] = roteadores_list[roteador]
            arvore[protoroteadores_list[base]][1] = roteadores[protoroteadores_list[base]][roteadores_list[roteador]]
    print(arvore)
