# Sample implementation of bubble sort
a = [23,4,51,12]

def bubble_sort(li):
    for index in range(len(li) -1 , 0, -1):
        for j in range(index):
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1], li[j]
    return li

print bubble_sort(a)
