# coding=utf-8

# import matplotlib.pyplot as plt
import math
def eye(m):
    w = []
    for i in range(m):
        w.append([0] *m)
    for i in range(len(w)):
        w[i][i] = 1
    return w

def dot(L1,L2):
    return sum(list(map(lambda x:x[0] * x[1],zip(L1,L2))))


def m_dot(M,L):
    m =[]
    for l in M:
        m.append(dot(l,L))
    return m

def lwlr(testpoint,dataset,labels,k=1.0):
    m= len(dataset)
    weight = eye(m)
    for i in range(m):
        diffArr = testpoint - dataset[i]
        weight[i][i]= math.exp(((diffArr*diffArr) **0.5)/(-2.0 *(k **2)))
    xTx = dot(dataset,m_dot(weight,dataset))
    thetas = 1/(xTx + 0.001)*dot(dataMat,m_dot(weight,labels))
    return thetas,testpoint*thetas


def lwlrTest(testArr,dataSets,labels,k = 1.0):
    m = len(testArr)
    yHat = [0] *m
    for i in range(m):
        thetas,pre= lwlr(testArr[i],dataSets,labels,k)
        yHat[i] = int(round(pre))
    return thetas,yHat

#接口，读取文件
def  loadData(filename):
    info = []
    dataMat = []
    labelMat = []
    fr = open(filename)
    for index,line in enumerate(fr.readlines()):
        line = line.strip("\n")
        line = line.split(":")
        dataMat.append(float(index))
        labelMat.append(float(line[1]))
    return dataMat,labelMat



def create_result(testMat_,dataMat_,labelMat_,k = 0.7):
    global testMat
    global dataMat
    global labelMat
    testMat = testMat_
    dataMat = dataMat_
    labelMat = labelMat_
    thetas, yHat2 = lwlrTest(testMat, dataMat, labelMat, k)
    return yHat2




# if __name__=="__main__":
    # dataMat, labelMat = loadData("../color.txt")
    # testMat = []
    # for j in range(71, 92):
    #     testMat.append(j)
    # thetas, yHat2 = lwlrTest(testMat, dataMat, labelMat, k=0.7)
    # plt.plot(range(len(testMat)), yHat2, "bo-")
    # plt.plot(range(len(dataMat)), labelMat, "ro-")
    # plt.xticks(range(len(dataMat)), dataMat, rotation=90)
    # plt.show()



