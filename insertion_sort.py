import numpy as np

def insertion_sort(list_):
    list_ = np.copy(list_)
    for i in range(1, len(list_)):
        key = list_[i]
        k = i
        while k > 0 and key < list_[k - 1]:
            list_[k] = list_[k - 1]
            k -= 1
        list_[k] = key
    return list(list_)


l = [1,5,8,2,4,9,10,3]
print(insertion_sort(l))
print(l)