# Implementation of the algorithm for validating balanced brackets in
# a C++ source file.

from lliststack import Stack

def isValidSource( srcfile ):
    s = Stack()
    for line in srcfile:
        for token in line:
            if token in "{[(":
                s.push( token )
            elif token in "}])":
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    print token, left
                    if ( token == '}' and left != '{' ) or \
                       ( token == ']' and left != '[' ) or \
                       ( token == ')' and left != '(' ):
                        return False
    return s.isEmpty()


if __name__ == '__main__':
    srcfile = open('cpp_srcfile.txt')
    print isValidSource( srcfile )
    srcfile.close()
