import numpy as np
from matplotlib import pyplot as plt

class RandomNumberGen:
    start_value = 3.531
    results_count = 200
    m = 700
    k = 99
    c = 0.02323

    @staticmethod
    def generate_numbers():
        x = np.zeros(1)
        x[0] = RandomNumberGen.start_value

        for i in range(1,RandomNumberGen.results_count):
            if(i<=RandomNumberGen.k):
                a = np.arange(i) +1
            else:
                a = np.append(a,0)

            tmp = a*np.flip(x)
            x = np.append(x,np.round(np.mod(tmp.sum() + RandomNumberGen.c, RandomNumberGen.m),3))
        #print(x)
        return x




