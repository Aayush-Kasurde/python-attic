# Sample examples of famous fizz buzz problem in python

print ['FizzBuzz' if not n % 15 else 'Fizz' if not n % 3 else 'Buzz' if not n % 5 else n for n in range(1,101)]

print["Fizz"*(i%3<1)+"Buzz"*(i%5<1)or i for i in range(1,101)]

for n in range(1,101):
    msg = ""
    if not (n%3):
        msg += "Fizz"
    if not (n%5):
        msg += "Buzz"
    print msg or str(n)

for i in range(1, 101):
    words = [word for n, word in ((3, 'Fizz'), (5, 'Buzz')) if not i % n]
    print ''.join(words) or i


print ('\n'.join(''.join(''.join(['' if i%3 else 'Fizz',
                                  '' if i%5 else 'Buzz']) 
                         or str(i)) 
                 for i in range(1,101)))

for i in range(1, 101):
  print 'Fizz'*(not(i%3))+'Buzz'*(not(i%5)) or i
