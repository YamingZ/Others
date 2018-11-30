import matplotlib.pyplot as plt
import math
import random

def plot_points(points, ax=None, style={'marker': 'o', 'color':'b'}, label=False):
    """plots a set of points, with optional arguments for axes and style"""
    if ax==None:
        ax = plt.gca()
    for ind, p in enumerate(points):
        ax.plot(p.real, p.imag, **style)
        if label:
            ax.text(p.real, p.imag, s=ind, horizontalalignment='center', verticalalignment='center')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)


def create_circle_points(n):
    """creates a list of n points on a circle of radius one"""
    return [math.cos(2 * math.pi * i / float(n)) + 1j * math.sin(2 * math.pi * i / float(n)) for i in range(n)]


def create_point_cloud(n):
    return [2 * random.random() - 1 + 1j * (2 * random.random() - 1) for _ in range(n//2)] + [1 * random.random() - 1 + 1j * (1 * random.random() - 1) for _ in range(n//2)]

def distance(A, B):
    return abs(A - B)

def incremental_farthest_search(points, k):
    remaining_points = points[:]
    solution_set = []
    solution_set.append(remaining_points.pop(random.randint(0, len(remaining_points) - 1)))
    for _ in range(k-1):
        distances = [distance(p, solution_set[0]) for p in remaining_points]
        for i, p in enumerate(remaining_points): #i下标，p元素
            for j, s in enumerate(solution_set):
                distances[i] = min(distances[i], distance(p, s))
        solution_set.append(remaining_points.pop(distances.index(max(distances))))
    return solution_set

def fps(points,k):
    remaining_points = points[:]
    solution_set = []
    distances = []
    distance_s = []
    solution_set.append(remaining_points.pop(random.randint(0, len(remaining_points) - 1)))
    for _ in range(k-1):
        for i,p in enumerate(remaining_points):
            for j,s in enumerate(solution_set):
                # print(distance(p,s))
                distance_s.append(distance(p,s))
            distances.append(sum(distance_s))
            # print("sum = " + str(sum(distance_s)))
            distance_s = []

        solution_set.append(remaining_points.pop(distances.index(max(distances))))
        distances = []
        # print(len(remaining_points),len(solution_set))

    return solution_set

#TODO: function distance


fig = plt.figure(figsize=(5, 5))
circle100 = create_circle_points(100)
cloud100 = create_point_cloud(20)

plot_points(circle100)
plot_points(incremental_farthest_search(circle100, 5), style={'marker': 'o', 'color':'r', 'markersize': 12})

plt.show()

