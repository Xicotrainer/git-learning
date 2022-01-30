import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def run():
    lst = [x+1 for x in range(89) if x%11 == 1]
    for l in lst:
        print("This is the sequence for all numbers under 89 with module 11: {}".format(l))

if __name__ == "__main__":
    run()