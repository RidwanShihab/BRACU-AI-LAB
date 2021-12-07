#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
pop=[]
result=[]


# In[2]:


n=int(input())
bankinfo=[]
population=[]
for i in range(n):
    x=input()
    bankinfo.append(x)
    if x[0]=="d":
          population.append(int(x[2:]))
    else:
          population.append(-1*int(x[2:]))
print(population)


# In[3]:


print(sum(population))


# In[9]:


def addPopulation(n):
    temp = [] 
    for i in range (0, n):
        temp.append(random.randint(0, 1))
    pop.append(temp)
    
def crossover(lis1, lis2):
    index = random.randint(0, n)
    for i in range (0, index):
        lis1[i], lis2[i] = lis2[i], lis1[i]
    fitness, values = calculateFitness(lis1)
    if(fitness != 0):
        lis1 = mutation(lis1)
    fitness, values = calculateFitness(lis2)
    if(fitness != 0):
        lis2 = mutation(lis2)
    return lis1, lis2

def calculateFitness(lis):
    values=[]
    
    i=0
    fitness=0
    while i < n:
              fitness=fitness+(lis[i]*population[i])
              i = i + 1

    values.append(lis)
    return fitness, values

def mutation(lis):
    a=random.randint(0, n-1)
    lis[a]=random.randint(0,1)
    return lis


# In[12]:


for i in range (0, n):
    addPopulation(n)
count = 0
while(True):
    count = count + 1
    x = random.randint(0, len(pop)-1)
    y = random.randint(0, len(pop)-1)
    
    pop[x], pop[y] = crossover(pop[x], pop[y])
    
    fitness, values =  calculateFitness(pop[x])

    if sum(values[0])!=0 and fitness == 0:
        result = pop[x]
        print(result,count)
        break;
    
    fitness, values =  calculateFitness(pop[y])

    if sum(values[0])!=0 and  fitness == 0:
        result = pop[y]
        print(result,count)
        break;
    if(count>100):
        print(-1)
        break;


# In[58]:





# In[59]:





# In[60]:





# In[ ]:




