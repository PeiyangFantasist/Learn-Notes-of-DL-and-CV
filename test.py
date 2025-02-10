import numpy as np
import pandas as pd
import random

ele = random.randint(1, 100)
def rand_array():
    arr=[]
    for i in range(3):
        arr.append(random.randint(1,100))
    return arr

def dim_array(dim):
    if dim == 1:
        return [random.randint(1, 100) for _ in range(3)]
    else:
        return [dim_array(dim - 1) for _ in range(3)]
    
def main():
    dim = input()
    result = dim_array(int(dim))
    with open('output.txt', 'w') as file:
        file.write(str(result))
    return result

if __name__ == "__main__":
    main()