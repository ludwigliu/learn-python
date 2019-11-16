# a python version of linux command pwd which prints 
# the current working directory

import os

def main():
    'Print the current working directory'
    print(os.path.abspath(os.path.curdir))

if __name__ == '__main__':
    main()