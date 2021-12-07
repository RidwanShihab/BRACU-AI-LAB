#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
population = []
result = []
def addPopulation():
    temp = [] 
    for i in range (0, 8):
        temp.append(random.randint(0, 7))
    population.append(temp)

def calculateFitness(lis):
    count = 0
    values = []
    for i in range (0,8):
        for j in range (i+1, 8):
            if(lis[i] == lis[j]):
                count = count + 1
                if lis[i] not in values:
                    values.append(lis[i])
            
            if((lis[j] - lis[i]) == (j - i)):
                count = count + 1
                if lis[i] not in values:
                    values.append(lis[i])

            if((lis[i] - lis[j]) == (j - i)):
                count = count + 1
                if lis[i] not in values:
                    values.append(lis[i])
    fitness = 28-count
    return fitness, values

def crossover(lis1, lis2):
    index = random.randint(0, 7)
    for i in range (0, index+1):
        lis1[i], lis2[i] = lis2[i], lis1[i]
    fitness, values = calculateFitness(lis1)
    if(fitness != 28):
        lis1 = mutation(lis1, values)
    fitness, values = calculateFitness(lis2)
    if(fitness != 28):
        lis2 = mutation(lis2, values)
    return lis1, lis2

def mutation(lis, values):
    n = random.randint(0, len(values)-1)
    idx = lis.index(values[n])
    x = random.randint(0, 7)
    while(x == values[n]):
        x = random.randint(0, 7)
    lis[idx] = x
    return lis

for i in range (0, 8):
    addPopulation()
count = 0
while(True):
    count = count + 1
    x = random.randint(0, len(population)-1)
    y = random.randint(0, len(population)-1)
    while y==x:
        y = random.randint(0, len(population)-1)
    
    population[x], population[y] = crossover(population[x], population[y])
    
    fitness, values =  calculateFitness(population[x])
    if fitness == 28:
        result = population[x]
        break;
    
    fitness, values =  calculateFitness(population[y])
    if fitness == 28:
        result = population[x]
        break;
        
print(result)


p=result


# In[5]:


atkr=0
for c in range(0, len(p)):
    for d in range(c+1, len(p)):
        if(p[c]==p[d]):
            atkr +=1
        if(abs(c-p[c])==abs(d-p[d])):
            atkr +=1
print(atkr)


# In[ ]:




