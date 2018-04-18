import matplotlib.pyplot as plt
def Draw(yHat2,dataMat,labelMat):
    print(len(labelMat))
    # plt.plot(range(len(labelMat)-len(yHat2)), [0]*(len(labelMat)-len(yHat2)), "go-")
    plt.plot(range(len(yHat2)), yHat2, "go-")
    plt.plot(range(len(labelMat) ), labelMat , "ro-")
    plt.xticks(range(len(dataMat)), dataMat, rotation=90)
    plt.show()