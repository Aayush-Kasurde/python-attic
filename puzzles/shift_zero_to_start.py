# Shift all zero to start of array without
# using any intermediate array

a = [2,3,0,8,4,0,2,1,2,3,0]
print "Before shifting zeroes to start " , a
count = len(a) - 1
for i in range(len(a), 0, -1):
    i = i - 1
    if a[i] != 0:
        a[count] = a[i]
        count = count - 1
        
while count > -1:
    a[count] = 0
    count = count - 1

print "After shifting zeroes to start  ", a


print "Before shifting zeroes to start " , a
a = [2,3,0,8,4,0,2,1,2,3,0]
count = 0
for i,v in enumerate(a):
    if v == 0:
        del a[i]
        a.insert(0,0)
print "After shifting zeroes to start  ", a
