""" Exploring yield!"""


def count(start, end=None):
    i = start

    while i <= end or end == None:
        yield i
        i += 1

c = count(1,10)

print c
print c.next()
print c.next()

infinite_yield=count(1)

for i in range(20):
    print infinite_yield.next()