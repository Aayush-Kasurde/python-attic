def partition(lst, start, end):
    pos = start
    print "Position : ", pos
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[pos] = lst[pos], lst[i]
            pos += 1
    lst[pos], lst[end] = lst[end], lst[pos]
    return pos

def quick_sort(lst, start, end):
    if start < end:
        pos = partition(lst, start, end)
        quick_sort(lst, start, pos - 1)
        quick_sort(lst, pos + 1, end)

def main():
    example = [3,45, 1,2,34]
    quick_sort(example, 0, len(example)- 1)
    print example

main()
