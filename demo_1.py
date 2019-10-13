import math
import numpy as np
import matplotlib.pyplot as plt

#def h(theta0,theta1,x):
#    return theta0 +theta1*x

def h1(theta,x):
    return theta[0]+theta[1]*x

def diff_0(theta,a):
    m=len(a)
    diff= 0;
    for i in a:
        diff=diff+(h1(theta,i[0])-i[1])
    diff=diff*(1/m)
    return diff

def diff_1(theta,a):
    m=len(a)
    diff= 0;
    for i in a:
        diff=diff+(h1(theta,i[0])-i[1])*i[0]
    diff=diff*(1/m)
    return diff

def cost(theta,a):
    m = len(a)
    cost=0;
    for i in a:
        cost=cost + (h1(theta,i[0])-i[1])**2
    cost=cost*(1/(2*m))
    return cost

def gradient1(alpha,theta,a):
    J_history = [cost(theta,a)]
    for i in range(10000):
        theta0 = theta[0] - alpha*diff_0(theta,a)
        theta1 = theta[1] - alpha*diff_1(theta,a)
        theta = [theta0,theta1]
        J = cost(theta,a)
        J_history.append(theta)
    return theta,J_history

# def gradient(m,alpha, theta0, theta1,input):
#     history=np.array([[]]) 
#     history=np.append(history, np.array([[theta0, theta1]]), axis=1)
#     j=[cost(m,theta0,theta1,input)]

#     for i in range(1000):
#         theta0_new = theta0 - alpha*diff_0(theta0,theta1,input)
#         theta1_new = theta1 - alpha*diff_1(theta0,theta1,input)
#         history=np.append(history, np.array([[theta0_new, theta1_new]]), axis=0)
#         theta0=theta0_new
#         theta1=theta1_new
#         j.append(cost(m,theta0,theta1,input))

#     return history,j

#collect input
if __name__ == "__main__":
    input=np.array([[]])
    with open('ex1data1.txt','r') as f:
        line=f.readline()
        line=line.rstrip("\n")
        line_split=line.split(",")
        
        input=np.append(input, np.array([[float(line_split[0]), float(line_split[1])]]), axis=1)
        for line in f:
            line=line.rstrip("\n")
            line_split=line.split(",")
            input=np.append(input, np.array([[float(line_split[0]), float(line_split[1])]]), axis=0)

    # input=input.T #transpose matrix from 97x2 to 2x97
    i=input.T
    print(i)
    # plt.figure(1)
    # plt.plot(i[0],i[1],'.r')
    # plt.show()
    alpha = 0.001
    theta = [0.0,0.0]
    a,p=gradient1(alpha,theta,input)
    print(a)
    plt.figure(2)
    plt.scatter(i[0],i[1],s=30,c='r',marker='x',linewidths=1)
    #print(h1(theta,i[0]))
    plt.plot(i[0],h1(a,i[0]))
    plt.show()
    