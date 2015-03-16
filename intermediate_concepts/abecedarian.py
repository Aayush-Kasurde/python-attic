#!/usr/bin/env python 
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c
    return True

print "accegj is abecdarian = "  , is_abecedarian('accegj')
print "bob is abecdaria = " , is_abecedarian('bob')

