from main import *
import math

def genNet(row,col,problem):
    """build an random net"""
    if problem == 1 or problem == 3:
        return np.random.rand(row, col)
    if problem == 2:
        net = np.random.rand(row,col,13)
        return net

def euclidean(selected,net,problem):
    """calculate euclidean distance"""
    if problem == 1 or problem == 3:
        return np.linalg.norm(net - selected, axis=1)
    if problem == 2:
        return np.linalg.norm(net - selected, axis=2)

def localize(center,sigma,domain,problem,net):
    """find the neighborhood and adjust it"""
    if sigma < 1:
        sigma = 1
    if problem == 1 or problem == 3:
        a =np.arange(domain)
        deltas = np.absolute(center - np.arange(domain))
        d= np.minimum(deltas, domain - deltas)
        a = np.exp(-(d*d) / (2 * (sigma*sigma)))
        return np.exp(-(d*d) / (2 * (sigma*sigma)))
    if problem == 2:
        delta_array = np.empty((15,15))
        for i in range(15):
            for j in range(15):
                delta_array[j][i]= math.sqrt((center[0]-i)**2+(center[1]-j)**2)

        d = delta_array
        this = -(d * d) / (2 * (sigma * sigma))
        return np.exp(this)

def som2Main(input, epoch, closeMethod,lr,pivot,sigma,problem,labels):
    """ run SOM to create activation map and class map"""
    n = input.shape[0]*pivot
    print(n)
    if problem == 1 or problem == 3:
        net=genNet(n,input.shape[1],problem)
    if problem == 2:
        n=15
        net = genNet(n,n,problem)
        activationMap = np.zeros((n,n))
        classMap = np.zeros((n,n,2))

    for i in range(epoch):
        if i % 1000 ==0:
            print("epoch: " + str(i))
        r = np.random.randint(0,input.shape[0])
        selected=input[r]
        if problem == 2:
            label = labels[r]
            if label[0] == 1:
                label = 1
            elif label[1] == 1:
                label = 2
            elif label[2] == 1:
                label = 3
        if closeMethod=='manhattan':
             eucl=euclidean(selected,net,problem)
             if problem == 1 or problem ==3:
                minVal=min(eucl)

                minNdx = eucl.argmin()
             if problem == 2:
                 minNdx = np.where(eucl == np.min(eucl))
                 y = minNdx[0][0]
                 x = minNdx[1][0]
                 activationMap[y,x]+=1

                 classMap[y,x,0] += int(label)
                 classMap[y,x,1] += 1

        if problem == 1 or problem == 3:
            localGuass=localize(minNdx,n//sigma,net.shape[0],problem,net)
            net += lr * localGuass[:, np.newaxis] * (selected - net)
        if problem == 2:
            localGuass = localize((x,y), n // sigma, net.shape[0],problem,net)
            newGuass = np.dstack([localGuass,localGuass])
            for i in range(11):
                newGuass = np.dstack([newGuass,localGuass])
            a = lr*newGuass
            b = (selected - net)
            c = a*b
            net += c

        lr = lr * 0.9999
        n = n * 0.999
    if problem == 1 or problem == 3:
        return net
    if problem == 2:
        return activationMap,classMap
