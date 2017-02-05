import random
import numpy as np

SAMPLES = 100000

FLIPS1 = 10
FLIPS2 = 500
FLIPS3 = 200

q2UPBOUND1 = 6
q3LOWBOUND1 = 5

q4UPBOUND1 = 5
q4NUMHEADS1 = 5

q2UPBOUND2 = 250
q3LOWBOUND2 = 5

q4UPBOUND3 = 100
q4NUMHEADS3 = 100

def coins(flips):
    return [1 if random.random()<0.6 else 0 for _ in range(flips)]

def splits(coins):
    splits = 1
    for n in range(len(coins)-1):
        if coins[n]!=coins[n+1]:
            splits+=1
    return splits

def stats(coins):
    return (splits(coins),np.sum(coins))

totflips1 = 0
q2num1=0
q3den1=0
q4num1=0

for _ in range(SAMPLES):
    groups, heads = stats(coins(FLIPS1))
    totflips1 += groups
    if groups > q2UPBOUND1:
        q2num1+=1
    if groups > q3LOWBOUND1:
        q3den1+=1
    if groups > q4UPBOUND1 and heads > q4NUMHEADS1:
        q4num1+=1

totflips2 = 0
q2num2=0
q3den2=0

for _ in range(SAMPLES):
    groups = splits(coins(FLIPS2))
    totflips2 += groups
    if groups > q2UPBOUND2:
        q2num2+=1
    if groups > q3LOWBOUND2:
        q3den2+=1

q4num3=0
for _ in range(SAMPLES):
    groups, heads = stats(coins(FLIPS3))
    if groups > q4UPBOUND3 and heads > q4NUMHEADS3:
        q4num3+=1

ans = [totflips1,q2num1,q3den1,q4num1,totflips2,q2num2,q3den2,q4num3,SAMPLES]
        
np.savetxt("s"+str(SAMPLES)+".dat",ans)

