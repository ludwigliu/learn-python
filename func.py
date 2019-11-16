# a simple function

def aFunction():
    # the fisrt line of string will be treated as part of the function
    # which can be referenced by f.__doc__
    '''A simple function to show the usage of function'''
    pass

def plus(x):
    return lambda y : y + x

def generalFunction(**parameters):
    return 'Once upon a time, there was a '\
        '%(job)s called %(name)s.' % parameters

def main():
    print(aFunction.__doc__)
    plusTen = plus(10)
    print(plusTen(22))
    print(generalFunction(job='king', name='ludwig'))


if __name__ == '__main__':
    main()