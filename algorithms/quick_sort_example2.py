
def quick_sort(items):
    if len(items) > 1:
        pivot_index = len(items) / 2
        smaller = []
        larger  = []

        for i, val in enumerate(items):
            if i != pivot_index:
                if val < items[pivot_index]:
                    smaller.append(val)
                else:
                    larger.append(val)
        quick_sort(smaller)
        quick_sort(larger)

        items[:] = smaller + [items[pivot_index]] + larger

def main():
    alist = [20,31,33,12,14,67, 1754]
    print alist
    quick_sort(alist)
    print alist
main()
