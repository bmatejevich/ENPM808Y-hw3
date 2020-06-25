from main import *
from matplotlib.path import Path

def prb3main():
    """coverage planning of H shaped area"""
    HPoints = np.array([
        [0, 0],
        [1, 0],
        [1, 1],
        [2, 1],
        [2, 0],
        [3, 0],
        [3, 3],
        [2, 3],
        [2, 2],
        [1, 2],
        [1, 3],
        [0, 3],
        [0, 0]

    ])

    plt.plot(HPoints[:, 0], HPoints[:, 1])
    x, y = np.meshgrid(np.arange(0, 3, .1), np.arange(0, 3, .1))  # make a canvas with coordinates
    x, y = x.flatten(), y.flatten()
    points = np.vstack((x, y)).T
    p = Path(HPoints)
    grid = p.contains_points(points)
    counter = 0
    arrayofpoints = []
    for bool in grid:
        if bool:
            xin = points[counter, :][0]
            yin = points[counter, :][1]
            arrayofpoints.append([xin, yin])
        counter += 1

    inside = np.array(arrayofpoints)
    route = som2Main(input=inside, epoch=10000, closeMethod='manhattan', lr=1.2,pivot=10,sigma=10,problem =3,labels = None)
    plt.plot(HPoints[:, 0], HPoints[:, 1])
    plt.plot(route[:, 0], route[:, 1], color='r', markersize=2)

    plt.show()
