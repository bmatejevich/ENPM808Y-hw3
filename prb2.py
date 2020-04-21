from ENPM808Y_HW3_Main import *
import re
import ast
np.set_printoptions(suppress=True)

def prepData(data):
    f = open(data, "r")

    count = 0
    dataOut = []
    for row in f:

        if count == 0:
            count = count + 1

        else:
            row = re.sub('\s+', ',', row)

            row = list(ast.literal_eval(row))

            count = count + 1

            dataOut.append(row)

    dataOut=np.asarray(dataOut)

    return dataOut


def prb2main():
    wineDesired = prepData('Wine Data/Wine Desired.asc')


    wineInput = prepData('Wine Data/Wine Input.asc')

    PercentTrain=.80


    indexLin = np.arange(0, len(wineInput), 1)
    trainNdx = [indexLin[:int(len(indexLin) * PercentTrain)]]
    trainI = wineInput[trainNdx]

    train_labels = wineDesired[trainNdx]

    testNdx = np.transpose(np.asarray([indexLin[int(len(indexLin) * PercentTrain):]]))
    testI = wineInput[testNdx]
    # testO = wineDesired[testNdx]

    # plt.scatter(tspPoints[:, 0], tspPoints[:, 1])
    # plt.show()

    activationMap,classMap = som2Main(input=trainI, epoch=10000, closeMethod='manhattan', lr=.7,pivot=0,sigma=5,problem =2,labels = train_labels)

    norm = np.linalg.norm(activationMap)
    activationMap = activationMap / norm
    plt.imshow(activationMap, cmap='hot', interpolation='nearest')
    plt.show()
    newClassMap = np.zeros((15,15))
    for row in range(15):
        for col in range(15):
            value = classMap[row,col,0]
            count = classMap[row,col,1]
            if value == 0:
                newClassMap[row,col]=0
            else:
                newClassMap[row,col] = int(value/count)


    plt.imshow(newClassMap)
    plt.show()
