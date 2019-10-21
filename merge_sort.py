# -*- coding: utf-8 -*-
# Introduction to Algorithms - 3rd Edition
import numpy as np

def merge(A, p, q, r):
    print('entrada: ',A[p:q], A[q:r])
    n_1 = q-p
    n_2 = r-q
    L = [A[p+i] for i in range(n_1)]
    R = [A[q+j] for j in range(n_2)]
    L.append(10000)
    R.append(10000)
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    print('saida: ',A[p:q], A[q:r])


def mergeSort(A, p ,r):
    if p < r:
        q = int((p+r)/2.0)
        print('1: ',A[p:q])
        mergeSort(A, p, q)
        #print('1: ',A[p:q])
        print('2: ',A[q+1:r])
        mergeSort(A, q+1, r)
        #print('2: ',A[q+1:r])
        print('indice',p, q, r)
        merge(A, p, q, r)
        print('--------')


#l = [5,8,1,2,3,6,4,7]
l = [4,2,20,15,11,40,26,27,1,3]
mergeSort(l, 0, len(l)-1)
print(l)