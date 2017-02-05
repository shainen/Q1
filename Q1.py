import random
import numpy as np

FLIPS = 10
SAMPLES = 1000000

def coins(flips):
    return [1 if random.random()<0.6 else 0 for _ in range(flips)]

def splits(coins):
    splits = 1
    for n in range(len(coins)-1):
        if coins[n]!=coins[n+1]:
            splits+=1
    return splits


split_stats=[splits(coins(FLIPS)) for _ in range(SAMPLES)]

split_stats2=[splits(coins(FLIPS)) for _ in range(SAMPLES)]

np.savetxt("f"+str(FLIPS)+"s"+str(SAMPLES)+"1.dat",split_stats)
np.savetxt("f"+str(FLIPS)+"s"+str(SAMPLES)+"2.dat",split_stats2)
