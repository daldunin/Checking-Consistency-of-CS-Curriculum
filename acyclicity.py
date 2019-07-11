# Uses python3

import sys
import numpy


def acyclic_single(adj):
    isacyclic = 1

    explore(0)
    # print(post)
    for (v1, v2) in edges:
        if post[v1 - 1] <= post[v2 - 1]:
            isacyclic = 0
            break;
    return isacyclic


def acyclic(adj):
    isacyclic = 1

    for v in range(0, len(adj)):
        if not visited[v]:
            explore(v)
    # print(post)
    for (v1, v2) in edges:
        if post[v1 - 1] <= post[v2 - 1]:
            isacyclic = 0
            break;
    return isacyclic

def explore(v):
    # print('v: ', v)
    # print('clock: ', clock)
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            explore(w)
    postvisit(v)


def postvisit(v):
    global clock
    clock = clock + 1
    post[v] = clock


clock = 10


if __name__ == '__main__':

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = numpy.zeros((n, 1))
    post = numpy.zeros((n, 1))
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(int(not acyclic(adj)))
