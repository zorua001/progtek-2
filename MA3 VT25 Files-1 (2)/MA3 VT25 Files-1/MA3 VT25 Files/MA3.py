""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
import functools

def approximate_pi(n): # Ex1
    #n is the number of points
    # Write your code here
    n_c = 0
    for i in range(n):
        k = random.uniform(-1, 1)
        b = random.uniform(-1, 1)
        if k**2 + b**2 <= 1:
            n_c += 1
            plt.plot(k,b,'*',color = 'red')
        else:
            plt.plot(k,b,'*',color = 'blue')
            
    print(4*n_c/n)
    plt.show()
            
    return 4*n_c/n

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere 
    lst = [functools.reduce(lambda x,y : x**2+ y**2,[random.uniform(-1, 1) for i in range(d)]) for j in range(n)]
    canc = list(filter(lambda x : x <= 1, lst))
    print(2*d * len(canc)/n)
    return 2*d * len(canc)/n

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere 
    return m.pi**(d/2) /(m.gamma(d/2 + 1))

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
      #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    start = pc()
    with future.ProcessPoolExecutor() as ex:
        k = [n for i in range (np)]
        c = [d for i in range (np)]
        results = ex.map(sphere_volume, k,c)
        
        for r in results:
            print(r)

    stop = pc()
    return stop-start
#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    return 
    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
#    for n in dots:
#        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #Ex3
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
    print(sphere_volume_parallel1(n, d),  'seconds')

    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    
    

if __name__ == '__main__':
	main()
