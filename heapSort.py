# -*- coding: utf-8 -*-
# Introduction to Algorithms - 3rd Edition

def parent(i):
    return (i-1) // 2

def left(i):
    return 2*i+1

def right(i):
    return 2*(i+1)

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def heapify(A, i, heapsize=None):

    if heapsize is None:
        heapsize = len(A)

    l = left(i)
    r = right(i)
    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        swap(A, i, largest)
        heapify(A, largest, heapsize)

def build_heap(A):
    heapsize = len(A)
    for i in range((heapsize // 2), -1, -1):
        heapify(A, i, heapsize)

def heapsort(A):
    build_heap(A)
    heapsize = len(A)
    for i in range(len(A)-1, -1, -1):
        swap(A, 0, i)
        heapsize -= 1
        heapify(A, 0, heapsize)
    return A

l = [8,9,1,4,5,2,6,7,0,-1,3]
print(heapsort(l))