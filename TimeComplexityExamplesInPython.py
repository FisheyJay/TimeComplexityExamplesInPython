###############################################################################
# Time Complexity examples in Python ...
###############################################################################

###############################################################################
# O(1) - Constant Time: Given an Input Size n, it only takes a single step for
#        the algorithm to accomplish the task.
#
#      - Return Statements, initializing a variable, incrementing, assigning, etc.
#      - All of these simple operations take O(1) time.
# Pseudocode Example:
###############################################################################
arr = [1, 2, 3, 4]
print("")
print("O(1) - Constant Time " + str(arr[3]) + "\n")

###############################################################################
# O(log n) - Logarithmic Time: The number of steps it takes to accomplish the
#            task are decreased by some factor with each step.
#          - A Binary Search Algorithm is an Example:
# Pseudocode Example:
###############################################################################
for idx in range(0, 10, 2):
    pass
    print("O(log n) - Logarithmic Time - idx {} ".format(idx))
print("")
###############################################################################
# O(n) - Linear Time: The Running Time increases at most linearly with the size
#        of the input.
#      - Running time of the loop is at most the running time of the statements
#        in the loop times the number of iterations.
# Pseudocode Example:
###############################################################################
for idx in range(0, 10):
    pass
    print(" O(n) - Linear Time - idx {} ".format(idx))
print("")
###############################################################################
# O(n log n) - QuasiLinear Time: in many cases the n log n running time is
#              simply the result of performing a O(log n) operation n times.
#            - For example: binary tree sort creates a binary tree by inserting
#              each element of the n-sized array one by one.
#            - The average case of QuickSort, HeapSort and MergeSort rin in
#              O(n log n)
# Pseudocode Example:
###############################################################################
for idx in range(0, 10):
    for jdx in range(0, 10, 2):
        pass
        print(" O(n log n) - QuasiLinear Time - idx {} ".format(idx))
print("")
###############################################################################
# O(n squared) - Quadratic Time - Bubble Sort, Selection Sort & Insertion Sort
#              - Total running time of nested loops is running time of outer
#                loop multipled by the inner loop(s).
# Pseudocode Example:
###############################################################################
for idx in range(0, 10):
    for jdx in range(0, 10):
        pass
        print(" O(n squared) - Quadratic Time - idx {} ".format(idx))
print("")
###############################################################################
# O(2 to the power n) - Exponential Time: Such as when traversing all nodes in
#                       a Binary Search TYree
# Pseudocode Example:
###############################################################################
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        print(" O(2 to the power n) - Exponential Time - idx {} ".format(idx))
        return fib(n-2) + fib(n-1)

whatever = fib(9)
print("")
print("The result is equal to {} ".format(whatever))
###############################################################################
# O(n!) - Factorial Time: Common in generating Permutations
# Pseudocode Example:
###############################################################################
def fact(n):
    if n <= 1:
        return 1
    else:
        print(" O(2 to the power n) - Exponential Time - idx {} ".format(idx))
        return n * fact(n-1)
print("")
whatever = fact(4)
print("")
print("The result is equal to {} ".format(whatever))