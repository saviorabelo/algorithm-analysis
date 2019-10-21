# -*- coding: utf-8 -*-

def merge(A, lenA, B, lenB):
	i = 0
	j = 0
	list_ = list()
	while i < lenA and j < lenB:
		if A[i] <= B[j]:
			list_.append(A[i])
			i = i + 1
		else:
			list_.append(B[j])
			j = j + 1

	if i == lenA:
		for i in range(j, lenB):
			list_.append(B[i])

	if j == lenB:
		for i in range(i, lenA):
			list_.append(A[i])

	return list_

def mergeSort(L, lenL):
	if lenL == 1:
		return L

	center = int(lenL/2.0) #floor

	if lenL%2 == 0:
		A = mergeSort(L[0:center], center)
		B = mergeSort(L[center:], center)
		return merge(A, center, B, center) 
	else:
		A = mergeSort(L[0:center], center)
		B = mergeSort(L[center:], center+1)
		return merge(A, center, B, center+1)

l = [8,9,1,4,5,2,6,7,0,-1,3]
print(mergeSort(l, len(l)))
print(l)
