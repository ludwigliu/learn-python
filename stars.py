# star to extract parameters
alist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']

first, *others = alist
*others, last = alist

print(first)
print(last)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)
def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

print([m+n for m in 'ABC' for n in 'XYZ'])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [ s.lower() for s in L1 if isinstance(s, str) ]
print(L2)

def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a+b

g = fib()

for x in range(1, 200):
    if x < 201:
        print(next(g))
    else:
        break
