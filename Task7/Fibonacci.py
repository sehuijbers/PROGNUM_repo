#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

class fib:
    def __init__(self, maxim, dev, end): #define the names
        self.maximum = maxim
        self.devid = dev
        self.end = end

    def array(self):#make a fobonacci sequence with end value
        seq = [0, 1]
        for i in range(2, self.end):
            seq.append(seq[i-1] + seq[i-2])
        return np.array(seq)

    def divm(self): #make it divideble by a given number
        fibi = self.array() 
        mask = (fibi < self.maximum) & (fibi % self.devid == 0)
        fib_fin = fibi[mask]
        return fib_fin


f = fib(maxim=np.inf, dev=7, end=100)
results = f.divm()

print(f"The Fibonacci numbers smaller than {f.maximum} and divisible by {f.devid} are:")
print(results)

