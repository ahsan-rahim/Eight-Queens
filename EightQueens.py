# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 04:12:16 2020

@author: Ahsan Rahim
"""
import random
from random import choices , sample

def attacksNone(board , i):
    val=board[i]
    for j in range(8):
        if (j!=i):
            diff= abs(i-j)
            if(board[j]==val or board[j]==val+diff or board[j]==val-diff):
                return False
    return True            



def fitness(pool):
    fit=[]
    for board in pool:
        count=0
        for i in range(8):
            if(attacksNone(board,i)):
                count+=1
        fit.append(count) 
    return fit

p1 = sample(range(1,9) , 8)   
p2 = sample(range(1,9) , 8)
parents= [p1 , p2 ]

def createChildren(parents):
    child1 = parents[0][:4] + (parents[1][4:])
    child2 = parents[0][4:] + (parents[1][:4])
    child3 = parents[1][:4] + (parents[0][4:])
    child4 = parents[1][4:] + (parents[0][:4])
  #  print([child1 , child2 , child3 , child4])
    return [child1 , child2 , child3 , child4]



def Mutation(survived):    
    for x in survived:
        x[random.randint(0,7)]=random.randint(1,8)
    return survived            

def Solve(parents):
    fitnessVals=[]
    fmax=8
    while(fmax not in fitnessVals):    
        pool=createChildren(parents) + parents
        fitnessVals = fitness(pool)
        if(fmax in fitnessVals):
            return pool[fitnessVals.index(8)]
        #Survival Selection using roulette wheel selection where fitness values are the weights
        parents = choices(pool , weights=fitnessVals , k=2)
        #Mutation of the new chromosomes
        parents=Mutation(parents)
        print(parents)
        #population size limited to 2
        
print("\nA possible solution to the 8 Queens problem is\n" ,Solve(parents))    