"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    ### TODO
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb
    

def longest_run(mylist, key):
    ### TODO

    length = 0

    maxcount = 0



    for i in range(len(mylist)):

        if mylist[i] == key:

            length += 1

        else:
            length = 0
        if length > maxcount:
            maxcount = length
    return maxcount
    


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)

def longest_run_recursive(mylist, key):
    return longest_run_recursiveCalc(mylist, key)[2]
    
def longest_run_recursiveCalc(mylist, key):
    if len(mylist) == 0:
        return (0, 0, 0)

    if len(mylist) == 1:
        if mylist[0] == key:
            return (1, 1, 1)
        else:
            return (0, 0, 0)

    middle = len(mylist) // 2
    Lmax = longest_run_recursiveCalc(mylist[:middle], key)
    Rmax = longest_run_recursiveCalc(mylist[middle:], key)
    
    if Lmax[0] != middle:
        left = Lmax[0]  
    else: 
        left = Lmax[0] + Rmax[0]
        
    if Rmax[1] != len(mylist) - middle:
        right = Rmax[1] 
    else: 
        right = Rmax[1] + Lmax[1]
        
    midMax = Lmax[1] + Rmax[0]

    max_length = max(Lmax[2], Rmax[2], midMax)

    return (left, right, max_length)

print(longest_run_recursive([12,12,12,8,12,12,12,12,7,8], 12))
