import random
import numpy as np

FLIPS = 10
SAMPLES = 100000
q2UPBOUND = 6
q3UPBOUND = 6
q3LOWBOUND = 5
q4UPBOUND = 5
q4NUMHEADS = 5

def coins(flips):
    return [1 if random.random()<0.6 else 0 for _ in range(flips)]

def splits(coins):
    splits = 1
    for n in range(len(coins)-1):
        if coins[n]!=coins[n+1]:
            splits+=1
    return splits

def stats(coins):
    return [splits(coins),np.sum(coins)]

def just_sp(stat):
    return list(zip(*stat))[0]

def quest1(sp):
    return np.mean(sp)

def quest2(sp):
    num = 0
    den = len(sp)
    for fl in sp:
        if fl > q2UPBOUND:
            num+=1
    return num/den

def quest3num(sp):
    num = 0
    den = 0
    for fl in sp:
        if fl > q3UPBOUND:
            num+=1
    return num

def quest3den(sp):
    num = 0
    den = 0
    for fl in sp:
        if fl > q3LOWBOUND:
            den+=1
    return den

def quest4(st):
    num = 0
    den = len(st)
    for fl, he in st:
        if fl > q4UPBOUND and he > q4NUMHEADS:
            num+=1
    return num/den

def allquestsion(st):
    justflips = just_sp(st)
    return (quest1(justflips),quest2(justflips),quest3num(justflips),quest3den(justflips),quest4(st))


stats1=[stats(coins(FLIPS)) for _ in range(SAMPLES)]

stats2=[stats(coins(FLIPS)) for _ in range(SAMPLES)]

ans1=allquestsion(stats1)
ans2=allquestsion(stats2)

np.savetxt("f"+str(FLIPS)+"s"+str(SAMPLES)+"1.dat",ans1)
np.savetxt("f"+str(FLIPS)+"s"+str(SAMPLES)+"2.dat",ans2)
