from random import randint
import time


def areup(n_):
    if(round(n_) > n_):
        n_ = round(n_)
    if(round(n_) < n_):
        n_ = round(n_)+1
    n_ = int(n_)
    return n_

n, c, t = input().split(" ")
""
n = int(n); c = int(c); t = int(t); lista = []; maior = 0

# lista =  input().split(" ")

inicio = time.time()

for f in range(0,n):
    lista.append(randint(1, 100000))

lista = [int(i) for i in lista]

menorMaior = sum(lista)

if(c > n):
    c = n



#Versão 1.0
""" 
ValorFinal = 0;melhorOrg =[]

lisTaMax = []

inicio =  1; fim = n-(c-1)+1
taMax = n-(c-1)-(inicio-1)

if(len(lista) == n):
    for i in range(inicio, fim):
        lisChaves = []; lisTaMax = []
        
        lisChaves.append(lista[0:i]) 

        indexIni = i; indexFim = i; cont = 1; comp = 1; soma = 0; res = i

        if(c != 2):
            for itm in range(c-2): lisTaMax += [taMax]
        else:
            lisTaMax += [taMax]
        
        while (c>1):
            if (comp <= c-2 and comp > 0):
                indexFim += 1    
                lisChaves = lisChaves[:comp]
                lisChaves.append(lista[indexIni:indexFim])
                res = indexIni
                comp += 1
                indexIni = indexFim
                
            else:
                lisChaves = lisChaves[:c-1]
                lisChaves.append(lista[indexIni:n])
                soma = 0
                
                for x in lisChaves:
                    if (sum(x) > soma):
                        
                        soma = sum(x)

                if(menorMaior > soma):  
                    print(lisChaves)
                    menorMaior = soma

                if(len(lisChaves[1]) == lisTaMax[0]):
                    break

                comp -= 1
                indexIni = res
            
                while (len(lisChaves[comp]) == lisTaMax[comp-1] ):
                    comp -= 1
                    lisTaMax[comp] -= 1
                    
                    if(lisTaMax[:comp+1].count(0) == 1 ):
                        index = lisTaMax.index(0)
                        for f in  range(index, len(lisTaMax)):
                            lisTaMax [f] = lisTaMax[comp-1] - 1
                        
                    a = 0
                    for f in lisChaves[:comp]:
                        a += len(f)
                    indexIni = a
                    indexFim= len(lisChaves[comp])+a     
          
        else:
           
            menorMaior = sum(lisChaves[0])


        taMax -= 1
        
else:
    print("ERRROUUUUUUU!")

 """


#Versão 2.00
"""
def ultimaLista(listaMod, c_, max_):
    eleUse = len(listaMod)
    _iniFim = 0; l  = c_; valor = 0
    for _n in range(l):
        c_ -= 1 
        eleUse = len(listaMod[_iniFim:]) - c_
        if(_n < l-1):
            for _i in range( 1 , eleUse+1):
                if(sum(listaMod[_iniFim: _iniFim + _i]) > max_):
                    _iniFim =  _iniFim + _i-1
                    break
                if(_i == eleUse):
                    _iniFim =  _iniFim + _i
        else:
            valor = sum(listaMod[_iniFim:])

    return valor

def validador(_max, ini, fim, lista_, _c,_n):
    veri = False
    if(ini == 0):
        teste = ultimaLista(lista_[fim:], _c, _max)     
        if(teste <= _max):
            veri = True

    elif(fim == _n):
        teste = ultimaLista(lista_[:ini], _c, _max)     
        if(teste <= _max):
            veri = True
        
    else:
        listaMod1 = lista_[:ini]
        listaMod2 = lista_[fim:]
        if((len(listaMod1) == 1 or len(listaMod2) == 1) and (len(listaMod2)  != len(listaMod1))):
            if(len(listaMod1) != 1):
                teste1 = ultimaLista(listaMod1, _c-1, _max)
                teste2 = listaMod2[0]
            else:
                teste1 = listaMod1[0]
                teste2 = ultimaLista(listaMod2, _c-1, _max)

            if(teste1 <= _max and teste2 <= _max):
                veri = True
            
        elif(len(listaMod2)  == 1 == len(listaMod1)):
            teste1 = listaMod1[0]
            teste2 = listaMod2[0]
            if(teste1 <= _max and teste2 <= _max):
                veri = True
        else:
            _c1 = _c2 = _c-1; p1 = p2 = 1
            if(_c1 > len(listaMod1)):
                _c1 = len(listaMod1)
                p1 = _c- _c1
            if(_c2 > len(listaMod2)):
                _c2 = len(listaMod2)
                p2 = _c-_c2
            
            if(_c1 > _c2):
                for _i in range(p1,_c2+1):
                    teste1 = ultimaLista(listaMod1, _c1, _max)
                    teste2 = ultimaLista(listaMod2, _i, _max)
                    if(teste1 <= _max and teste2 <= _max):
                        veri = True
                        break
                    if(teste1 > _max):

                        break
                    _c1 -= 1
            else:
                for _i in range(p2,_c1+1):
                    teste1 = ultimaLista(listaMod1, _i, _max)
                    teste2 = ultimaLista(listaMod2, _c2, _max)
                    if(teste1 <= _max and teste2 <= _max):
                        veri = True
                        break
                    if(teste2 > _max):
                        break
                    _c2 -= 1


    return veri

con = 0

# print(lista)
if(c > 1):
    maxi = n-(c-1)
    listaPossi = {}; media =  sum(lista)/c

    for  tam in range(1, maxi+1):
        if(c > 2):
            cont = 0
            while(cont+tam <= n):
                if(sum(lista[cont: cont+tam]) >= media ):
                    listaPossi[cont, cont+tam] = sum(lista[cont: cont+tam])
                cont += 1
        else:
            if(sum(lista[0: tam]) >= media ):
                listaPossi[0, tam] = sum(lista[0: tam])
            if(sum(lista[tam: n]) >= media ):
                listaPossi[tam, n] = sum(lista[tam: n])
        print(tam)


    # print(listaPossi)
    while True:
        i = list(listaPossi.values()).index(min(list(listaPossi.values())))
        if(validador(list(listaPossi.values())[i], list(listaPossi.keys())[i][0], list(listaPossi.keys())[i][1], lista, c-1,n)):
            menorMaior = list(listaPossi.values())[i]
            break
        con += 1
        print(con)
        listaPossi.pop(list(listaPossi.keys())[i])

"""



#Versão 3.0
def ultimaLista(lista_, c_, max_,n_):
    prox_list  = []; volta_ = 1
    soma_ = 0; temp_ = c_-1
    ciclos = 0; n_ = n_-(c_-1)

    for key_ , i_ in enumerate(lista_):

        # print("i" , i_, "comp", temp_, "SOMA", soma_ )
        ciclos += 1

        if (temp_ == 0):
            if (soma_ > 0 ):
                key_ -= 1
            break

        soma_ += i_       

        if(soma_ > max_):
            prox_list.append(soma_-max_)
            soma_ = i_
            temp_ -= 1
            n_ += 1

        if (key_ == n_ -1):
            soma_ = 0 
            temp_ -= 1
            n_ += 1
        
        

    print(ciclos)
    volta_ = sum(lista_[key_:])        
    prox_list.append(volta_-max_)

    prox_ = min(prox_list)



   
    return prox_, volta_


if(c > 1):
 
    if (max(lista) > areup(sum(lista)/c)):
        valor = max(lista)
    else:
        valor = areup(sum(lista)/c)
        
    while True:
        # print(valor)
        prox ,ultima = ultimaLista(lista, c,valor, n) 
        if(ultima <= valor):
            menorMaior = valor
            break
        valor += prox




valorFinal = areup(menorMaior/t)
print(valorFinal)

fim = time.time()
print(fim - inicio)