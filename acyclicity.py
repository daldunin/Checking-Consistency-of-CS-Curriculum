# Uses python3

# Problem: Checking Consistency of CS Curriculum
# Problem Introduction
# A Computer Science curriculum specifies the prerequisites for each course as a list of courses that should be
# taken before taking this course. You would like to perform a consistency check of the curriculum, that is,
# to check that there are no cyclic dependencies. For this, you construct the following directed graph: vertices
# correspond to courses, there is a directed edge (𝑢, 𝑣) is the course 𝑢 should be taken before the course 𝑣.
# Then, it is enough to check whether the resulting graph contains a cycle.
# Problem Description
# Task. Check whether a given directed graph with 𝑛 vertices and 𝑚 edges contains a cycle.
# Input Format. A graph is given in the standard format.
# Constraints. 1 ≤ 𝑛 ≤ 103, 0 ≤ 𝑚 ≤ 103.
# Output Format. Output 1 if the graph contains a cycle and 0 otherwise.

import sys
import numpy

global clock

def acyclic_single(adj):
    isacyclic = 1

    explore(0)

    for (v1, v2) in edges:
        if post[v1 - 1] <= post[v2 - 1]: # according to theorem
            isacyclic = 0
            break;
    return isacyclic


def acyclic(adj):
    isacyclic = 1

    for v in range(0, len(adj)):
        if not visited[v]:
            explore(v)

    for (v1, v2) in edges:
        if post[v1 - 1] <= post[v2 - 1]:
            isacyclic = 0
            break;
    return isacyclic

def explore(v):
    visited[v] = 1
    for w in adj[v]:
        if not visited[w]:
            explore(w)
    postvisit(v)


def postvisit(v):
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
