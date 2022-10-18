#!/usr/bin/env python
# coding: utf-8

# # Condiciones para filtrar los grupos iniciales:

# In[ ]:


nDelGrupo = 10
container = list()
values = list()
values = [x for x in itertools.permutations(range(1,nDelGrupo +1),nDelGrupo )]

container.append(values[0])

for a in range(1,nDelGrupo ):
    for b in range(1,len(values)-1):
        if values[b][0] == 1 + a and values[b][-1] == nDelGrupo -a and values[b][0] != nDelGrupo :
            continuar = True
            for ab in range(nDelGrupo-1):
                
                if values[b][ab+1] == values[b][ab] +1:  # El siguiente no puede ser +1 del anterior
                    continuar = False
                    break
                    
                if values[b][ab+1] == values[b][ab] -1:  # El siguiente no puede ser -1 del anterior
                    continuar = False
                    break
                    
                if values[b][ab] + values[b][nDelGrupo-1-ab] != nDelGrupo + 1:  # Los complementarios tienen que sumar n+1
                    continuar = False
                    break
                    
            if continuar == True:
                aux.append(values[b])
                    
    if aux != list():
        container.append(aux)
    aux = list()
    
container.append(values[-1])

for x in container: 
    print(len(x))
for x in container[1]:
    print(x)



# # Mejorando la eficiencia del mapeado de pares de elementos:

# In[ ]:


import numpy.lib.stride_tricks 

nDelGrupo = 6

values = [x for x in itertools.permutations(range(1,nDelGrupo +1),nDelGrupo )]
perms = set(x for x in itertools.permutations(range(1,nDelGrupo +1),2))
len_perms = len(perms)

paresTotales = set()

for a in range(nDelGrupo ):
    for b in range(nDelGrupo ):
        if (b+1 <= nDelGrupo -1):
            c.add((matriz[a][b], matriz[a][b+1]))
            
print(len(c) == len_perms)


# In[ ]:


a = np.array([[1,2,3], [4,5,6]])
b = np.array([[1,4],[2,5],[3,6]])
print(b)
print(np.array_equal(a.transpose(),b))


# In[ ]:


((82258278193561600/1500000)/3600)/24



# In[ ]:


a = [1,["a","b"]]
b = [2,["c","d"]]
c = [[a,b] for x in a for y in b]
c


# In[ ]:


nDelGrupo = 8
container = list()
aux = list()
values = list()
values = [x for x in itertools.permutations(range(1,nDelGrupo +1),nDelGrupo )]
aux.append(values[0])
container.append(aux)
print(container)
aux = list()
for a in range(1,nDelGrupo ):
    for b in range(1,len(values)-1):
        if values[b][0] == 1 + a and values[b][-1] == nDelGrupo -a and values[b][0] != nDelGrupo :
            continuar = True
            for ab in range(nDelGrupo-1):
                
                if values[b][ab+1] == values[b][ab] +1:  # El siguiente no puede ser +1 del anterior
                    continuar = False
                    break
                    
                if values[b][ab+1] == values[b][ab] -1:  # El siguiente no puede ser -1 del anterior
                    continuar = False
                    break
                    
                if values[b][ab] + values[b][nDelGrupo-1-ab] != nDelGrupo + 1:  # Los complementarios tienen que sumar n+1
                    continuar = False
                    break
                    
            if continuar == True:
                aux.append(values[b])
                    
    if aux != list():
        container.append(aux)
    aux = list()

aux.append(values[-1])
container.append(aux)
print(container)
combs = list(itertools.product(*container))
for x in combs:
    print(x)


# In[ ]:


test =  [[1, 2, 3 ,4, 5, 6, 7, 8], [2, 5 ,8 ,6, 3 ,1 ,4, 7], [3, 8, 5, 2 ,7 ,4 ,1 ,6], [4 ,6 ,2, 8, 1 ,7, 3, 5], [5, 3, 7, 1, 8 ,2 ,6, 4], [6,1 ,4 ,7, 2, 5 ,8, 3], [7, 4 ,1, 3, 6, 8, 5, 2], [8, 7 ,6, 5, 4, 3, 2, 1]] 
c = set()
nDelGrupo = 8
perms = set(x for x in itertools.permutations(range(1,nDelGrupo +1),2))
len_perms = len(perms)

for matriz in resultados_preeliminares:
    for filas in matriz:
        for pares in itertools.pairwise(filas):
            c.add(pares)
    if c == perms:
        resultados_finales.append(resultado)
    c = set()

for x in resultados_finales:
    print(np.array(x))


# In[ ]:


resultados = list()
nDelGrupo = 8
container = list()
aux = list()
values = list()
values = [x for x in itertools.permutations(range(1,nDelGrupo +1),nDelGrupo )]
aux.append(values[0])

container.append(aux)
container.append(values[0])
aux = list()

perms = set(x for x in itertools.permutations(range(1,nDelGrupo +1),2))

for a in range(1,nDelGrupo ):
    for b in range(1,len(values)-1):
        if values[b][0] == 1 + a and values[b][-1] == nDelGrupo -a and values[b][0] != nDelGrupo :
            continuar = True
            for ab in range(nDelGrupo-1):

                if values[b][ab+1] == values[b][ab] +1:  # El siguiente no puede ser +1 del anterior
                    continuar = False
                    break

                if values[b][ab+1] == values[b][ab] -1:  # El siguiente no puede ser -1 del anterior
                    continuar = False
                    break

                if values[b][ab] + values[b][nDelGrupo-1-ab] != nDelGrupo + 1:  # Los complementarios tienen que sumar n+1
                    continuar = False
                    break

            if continuar == True:
                aux.append(values[b])

    if aux != list():
        container.append(aux)
    aux = list()

aux.append(values[-1])
container.append(aux)


start = time.time()

combs = list(x for x in itertools.product(*container))
    
"""for x in combs:
    cand = np.array(x, dtype = object)
    if np.array_equal(cand.transpose(), cand):
        print("\n", cand, "\n")
        #resultados.append(x)
"""
end = time.time()

print("cantidad de resultados: ", len(resultados))


print("\n-- Fin del calculo, tiempo transcurrido: ", float(end - start), "segs.")
#print("Operaciones por segundo: ,", len(combs)/(end-start) )


# In[ ]:


a = {(1,2),(3,4)}
b = {(3,4),(1,2)}
print(a == b)


# In[ ]:


a = [1,2,3,4]
b = np.fromiter(a, dtype = object)
c = np.array(a, dtype = object)
print(b)
print(c)


# In[ ]:


a = np.array([[[1,2,3,4],[2,4,1,3],[3,1,4,2],[4,3,2,1]], [[1,3,3,4],[2,1,3,4],[3,4,1,2],[4,3,2,1]]])
(np.array_equal(a[0].transpose(),a[0]))
b = a[np.array_equal(np.array(x for x in a).transpose(),np.array(x for x in a))]
print(b)
for x in a:
    print(x)



# In[873]:


from numpy.linalg import matrix_power
nDelGrupo =4
template = np.zeros((nDelGrupo, nDelGrupo))
grupoInicial = tuple(x for x in range(1,nDelGrupo+1))
print(grupoInicial)


# In[841]:


funcionPermutacion = []
for i in range(1,nDelGrupo):
    if i == 1:
        funcionPermutacion.append(1)
    if i == nDelGrupo-1:
        funcionPermutacion.append(-1)
    else:
        funcionPermutacion.append(2*pow(-1,i+1))
funcionPermutacion


# In[842]:


matrizPermutacion = np.zeros((nDelGrupo,nDelGrupo))
matrizPermutacion


# In[844]:


for x in range(nDelGrupo):
    #print("x aumenta su valor", x)
    for y in range(nDelGrupo):
        #print("y:", y, " - x+ FuncionPerm:", x+funcionPermutacion[x])
        if y == x+funcionPermutacion[x]:
            #print("Coinciden")
            matrizPermutacion[x][y] = 1
matrizPermutacion


# In[869]:


grupoInicial*matrix_power(matrizPermutacion,nDelGrupo)


# In[875]:


grupoInicial*matrix_power(matrizPermutacion,(nDelGrupo//2))


# In[871]:


for x in range(1,nDelGrupo/2):
    template += a = grupoInicial*(matrix_power(matrizPermutacion,nDelGrupo) + matrix_power(matrizPermutacion, nDelGrupo//2))*matrix_power(matrizPermutacion, 


# In[884]:


a = grupoInicial*(matrix_power(matrizPermutacion,nDelGrupo) + matrix_power(matrizPermutacion, nDelGrupo//2))
a


# In[882]:


a*(matrix_power(matrizPermutacion,nDelGrupo) + matrix_power(matrizPermutacion, nDelGrupo//2 +1))

