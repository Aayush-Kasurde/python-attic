# Sample implementation of quick sort
a = [23,4,51,12]

def quick_sort(items):
    if len(items) > 1:
        pivot = len(items) / 2
        smaller = []
        larger = []
        for i, val in enumerate(items):
            if i != pivot:
                    if val < items[pivot]:
                        smaller.append(val)
                    else:
                        larger.append(val)
        quick_sort(smaller)
        quick_sort(larger)
        items[:] = smaller + [items[pivot]] + larger
    return items
print quick_sort(a)