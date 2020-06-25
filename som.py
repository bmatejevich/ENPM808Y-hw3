from main import *


def genNet(var):
    return np.random.rand(var, 2)


def sommain(input, output, itr):
    """build SOM"""
    nbd = 6
    contractnbd = 1
    count = 0
    for epoch in range(itr):
        count = count + 1;
        eta = 0.9 * (1 - epoch / 1000)
        if epoch > 999:
            eta = 0.005
        for p in range(numpats):
            for indx in range(maxneuron):
                for indy in range(maxneuron):
                    dist[indx, indy] = np.sqrt(
                        (instarx[indx, indy] - data[0, p]) ^ 2 + (instary[indx, indy] - data[2, p]) ^ 2)

        [val1, rows] = min(dist)
        [val2, cols] = min(val1)
        indxmin = rows[cols]
        indymin = cols

        for i in range(indxmin - nbd, indxmin + nbd):
            for j in range(indymin - nbd, indymin + nbd):
                if i >= 1 and i <= maxneuron and j >= 1 and j <= maxneuron:
                    instarx[i, j] = instarx[i, j] + eta * (data[0, p] - instarx[i, j])
                    instary[i, j] = instary[i, j] + eta * (data[1, p] - instary[i, j])

        for i in range(maxneuron):
            for j in range(maxneuron):
                nb = np.array([
                    [1, i - 1, j],
                    [2, i + 1, j],
                    [3, i, j - 1],
                    [4, i, j + 1]
                ])
                for k in range(3):
                    if nb[k, 1] >= 1 and nb[k, 1] <= maxneuron and nb[k, 2] >= 1 and nb[k, 2] <= maxneuron:
                        None
                        # line([instarx(i, j), instarx(nb(k, 2), nb(k, 3))],[instary(i, j), instary(nb(k, 2), nb(k, 3))]);

            if count == 200:
                nbd = nbd - contractnbd
                if nbd < 1:
                    nbd = 1

                count = 0
    return route
