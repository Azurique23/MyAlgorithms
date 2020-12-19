
def jogador(_lista):
    if 23 in _lista:
        _lista = _lista[:len(_lista)-1]
    _lista = sorted(_lista, reverse = True); TF = True
    for _i in _lista:
        if(_lista.count(_i) == 3):
            while _i in _lista:
                _lista.remove(_i)
            TF = False
            break
    if(TF):
        for _i in _lista:
            if(_lista.count(_i) == 2):
                while _i in _lista:
                    _lista.remove(_i)
                if(len(_lista)== 2):
                    break
    _lista = sorted(_lista)

    _valor = _lista[0]
    return _valor
    
n, k = input().split(" ")
n = int(n); k = int(k); lista = []; passCoringa = False; V1 = True; estadoV = {}

for i in range(n):
    lista.append(list(input()))

for key,i in enumerate(lista):
    while "A" in i:
        i[i.index("A")] = 1
        lista[key] = i
    while "D" in i:
        i[i.index("D")] = 10
        lista[key] = i
    while "Q" in i:
        i[i.index("Q")] = 11
        lista[key] = i
    while "J" in i:
        i[i.index("J")] = 12
        lista[key] = i
    while "K" in i:
        i[i.index("K")] = 13
        lista[key] = i

    lista[key] = list(int(z) for z in lista[key] )

a = lista[k-1]; a.append(23); lista[k-1] = a; cont = 0

for key, i in enumerate(lista):
    if(i.count(i[0]) == len(i)):
        V1 = False
        estadoV[key] = sum(i)

if(V1):
    while not((lista[k-1][0] == lista[k-1][1] == lista[k-1][2] == lista[k-1][3] or lista[k-1][1] == lista[k-1][2] == lista[k-1][3] == lista[k-1][4]) and (23 not in lista[k-1] or passCoringa)):
        if (passCoringa and len(lista[k-1]) == 5):
            if(k == n):
                jogador1 = lista[k-1]
                jogador2 = lista[0]; jogador2.append(jogador1[4])
                jogador1.remove(23) 
                jogador1 = sorted(jogador1);jogador2 = sorted(jogador2)
                lista[k-1] = jogador1
                lista[0] = jogador2
                k = 1
                cont = 0
                passCoringa = False
            else:
                jogador1 = lista[k-1]
                jogador2 = lista[k]; jogador2.append(jogador1[4])
                jogador1.remove(23) 
                jogador1 = sorted(jogador1);jogador2 = sorted(jogador2)
                lista[k-1] = jogador1
                lista[k] = jogador2
                k += 1
                cont = 0
                passCoringa = False
        else:
            if(k == n):
                jogador1 = lista[k-1]
                jogador2 = lista[0];  jogador2.append(jogador(jogador1))
                jogador1.remove(jogador(jogador1))
                jogador1 = sorted(jogador1);jogador2 = sorted(jogador2)
                lista[k-1] = jogador1
                lista[0] = jogador2
                k = 1
                if(cont == n-1):
                    passCoringa = True
                cont += 1
            else:
                
                jogador1 = lista[k-1]
                jogador2 = lista[k];  jogador2.append(jogador(jogador1))
                jogador1.remove(jogador(jogador1))
                jogador1 = sorted(jogador1);jogador2 = sorted(jogador2)
                lista[k-1] = jogador1
                lista[k] = jogador2
                k += 1
                if(cont == n-1):
                    passCoringa = True
                cont += 1

else:
    k = min(estadoV.keys())+1
print(k)