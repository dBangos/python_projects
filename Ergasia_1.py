#creating an array of random numbers from 1 to 6
import random
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np #Needed for matrix calulations
dice_values = [1, 2, 3, 4, 5, 6]

def dice_array(arr_size):
    arr = []
    for x in range(0, arr_size):
        arr.append(random.randint(1, 6))
    return arr
#Calculating the probability density function of an array of integers
def pdf(arr, val_range):
    p = [0]*val_range
    for x in range(0, len(arr)):
        p[arr[x]-1] = p[arr[x]-1] + 1 #Array p now has the number of times each number shows up in the array arr
    p[:] = [x / len(arr) for x in p] #Array p now shows the probability of each number appearing in arr
    return p
def jointpdf(arr1, arr2, val_range):
    jp = np.zeros((val_range, val_range))
    for x in range(0, len(arr1)):
        jp[arr1[x]-1][arr2[x]-1] = jp[arr1[x]-1][arr2[x]-1]+1
    jp = jp/len(arr1)
    return jp


def gradient_descent(derivf, learning_rate, x0, error_threshold):
    x1 = x0-learning_rate*derivf(x0)
    i = 0
    while(abs(x1-x0)>=error_threshold):
        i = i+1
        x0 = x1
        x1 = x0-learning_rate*derivf(x0)
        if (x1 > 10000):
            print('Terminated to avoid overflow.')
            i = 0
            break
    return x1, i

def gradient_descent_newton(derivf, second_der_rev, x0, error_threshold):
    x1 = x0-second_der_rev(x0)*derivf(x0)
    i = 0
    while(abs(x1-x0)>=error_threshold):
        i = i+1
        x0 = x1
        x1 = x0-second_der_rev(x0)*derivf(x0)
    return x1, i

def demo2_1():
    demonstration_values = [20, 100, 1000]
    for i in demonstration_values:
        arr=dice_array(i)
        p=pdf(arr,6)
        plt.xlabel('Dice Value')
        plt.ylabel('Probability')
        plt.bar(dice_values, p)
        plt.show()

def demo2_2():
    demonstration_values = [10, 20, 50, 100, 1000]
    for i in demonstration_values:
        x = dice_array(i)
        px = pdf(x, 6)
        dx = scipy.stats.rv_discrete(values=(dice_values, px))
        print('Expected Value:',dx.expect(), 'Variance:',dx.var(), 'Skewness:',scipy.stats.skew(x), 'Kurtosis:',scipy.stats.kurtosis(x))

def demo3():
    z1 = dice_array(1000)
    z2 = dice_array(1000)
    jp = jointpdf(z1, z2, 6)
    print(jp)
    plt.matshow(jp)
    plt.show()
    y = np.add(z1, z2)
    newp = pdf(y, 12)
    plt.xlabel('Dice Value')
    plt.ylabel('Probability')
    plt.bar([1,2,3,4,5,6,7,8,9,10,11,12], newp)
    plt.show()

def derivative_demo(x):
    return 4*((x-5)**3)+3
def second_derivative_reversed(x):
    return 1/(12*((x-5)**2))

def demo4(steps, starting_point):
    print(gradient_descent(derivative_demo, 0.02, starting_point, 0.0001))
    print(gradient_descent_newton(derivative_demo, second_derivative_reversed, starting_point, 0.0001))
    a=[0]*steps
    count1=[0]*steps
    nn=[0]*steps
    for i in range(0, steps):
        nn[i]=0.00001*i
        a[i], count1[i] = gradient_descent(derivative_demo, 0.00001*i, starting_point, 0.0001)

    b, count2 = gradient_descent_newton(derivative_demo, second_derivative_reversed, starting_point, 0.0001)
    print(b, count2)
    print(a)
    print(count1)
    plt.plot(nn,count1)
    plt.show()


demo2_1()
demo2_2()
demo3()
demo4(30,40)