"""
Sometimes you don't need to store the result of a list comprehension in a variable
In this case, you can use generators#
"""

# generator exaumple
g = (x for x in range(4))

print type(g)


# generators can use the next method to return the following element of the list
# first element returned by next is the first element of the list
g2=(x*x for x in range(1,10))

print g2.next()
print g2.next()
print g2.next()
print g2.next()
print g2.next()
print g2.next()

for i in g:
    print i

# WATCH OUT: when using a generator, the pointer to the last generator number will be set to the last number of the sequence
# when trying to apply the next method, python will throw a StopIteration error!!!
print sum(g)

print g.next()