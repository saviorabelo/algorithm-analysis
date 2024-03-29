# -*- coding: utf-8 -*-
# Introduction to Algorithms - 3rd Edition

def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A


l = [8,9,1,4,5,2,6,7,0,-1,3]
print(insertionSort(l))
