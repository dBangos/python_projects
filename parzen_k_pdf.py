import numpy as np
import matplotlib as plt

def parzen_window(inputarray,h,lowlimit,highlimit):#h is the desired bin width, lowlimit/highlimit the smallest/greatest value for the pdf
    ll = lowlimit;
    resultarray = []
    k=0
    while(ll<highlimit+h/2):
        resultarray.append(0)
        for i in range(len(inputarray)):#for every element of the array
            resultarray[k] = resultarray[k] + np.exp(-(ll-inputarray[i])*np.transpose(ll-inputarray[i])/(2*np.power(h,2)))
        resultarray[k] = resultarray[k]*(1/len(inputarray)*(1/((np.power((2*np.pi),(1/2)))*(h))))
        k = k+1
        ll = ll+h
    return resultarray

def parzen_example(h,N):
    s = 2*np.random.random(N)
    b = parzen_window(s, h, -1, 3)
    return b
"""
a1=parzen_example(0.05,32)
a2=parzen_example(0.2,32)
a3=parzen_example(0.05,256)
a4=parzen_example(0.2,256)
a5=parzen_example(0.05,5000)
a6=parzen_example(0.2,5000)
plt.plot(a1)
plt.show()
plt.plot(a3)
plt.show()
plt.plot(a5)
plt.show()
plt.plot(a2)
plt.show()
plt.plot(a4)
plt.show()
plt.plot(a6)
plt.show()
"""

def k_nearest_neighbour(inputarray,knn,lowlimit,highlimit,step):#knn is the desired number of neighbours, lowlimit/highlimit the smallest/greatest value for the pdf
    k = 0
    resultarray = []
    ll = lowlimit
    while (ll < highlimit + step / 2):
        temp=[]
        for i in range(0,len(inputarray)):
            temp.append(0)
            temp[i] = np.sqrt(np.power((ll-inputarray[i]),2))
        temp.sort()
        resultarray.append(0)
        resultarray[k]=knn/(len(inputarray)*2*temp[knn-1])
        k = k+1
        ll = ll + step
    return resultarray


def knn_example(k):
    s = 2 * np.random.random(5000)
    b = k_nearest_neighbour(s, k, -1, 3, 0.01)
    return b

"""
b1=knn_example(32)
b2=knn_example(64)
b3=knn_example(256)
plt.plot(b1)
plt.show()
plt.plot(b2)
plt.show()
plt.plot(b3)
plt.show()
"""
def knn_classifier(Z,v,K,x):
    c=max(v)
    for i in range(len(Z)):
        dist=(x[i]-Z)^2




def example_four_two():
    xi=[]
    xclass=[]
    for i in range(0,100):
        a=np.random.random()
        xi.append(0)
        xclass.append(0)
        if a<0.5:
            xi[i]=np.random.normal(2,0.5,1)
            xclass[i]=1
        elif 0.5<=a<=0.8:
            xi[i] = np.random.normal(1, 1, 1)
            xclass[i]=2
        else:
            xi[i] = np.random.normal(3, 1.2, 1)
            xclass[i] = 3
    yi=[]
    for i in range(0, 1000):
        a = np.random.random()
        yi.append(0)
        if a < 0.5:
            yi[i] = np.random.normal(2, 0.5, 1)
        elif 0.5 <= a <= 0.8:
            yi[i] = np.random.normal(1, 1, 1)
        else:
            yi[i] = np.random.normal(3, 1.2, 1)
    
    a1 = parzen_window(yi, 0.01, -3, 6)
    a2 = parzen_window(yi, 0.1, -3, 6)
    a3 = parzen_window(yi, 0.5, -3, 6)
    a4 = parzen_window(yi, 1, -3, 6)
    plt.plot(a1)
    plt.show()
    plt.plot(a2)
    plt.show()
    plt.plot(a3)
    plt.show()
    plt.plot(a4)
    plt.show()
    b1 = k_nearest_neighbour(yi, 1, -2, 5, 0.01)
    b2 = k_nearest_neighbour(yi, 2, -2, 5, 0.01)
    b3 = k_nearest_neighbour(yi, 3, -2, 5, 0.01)
    #plt.plot(b1)
    #plt.show()
    plt.plot(b2)
    plt.show()
    plt.plot(b3)
    plt.show()



example_four_two()