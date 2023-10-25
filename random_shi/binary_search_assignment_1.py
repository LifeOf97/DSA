""" State the problem clearly. Identify the input & output formats.

Write a program to get the minimum number of times a sorted (ascending) list was rotated,
assuming all numbers in the list are unique.

input: A rotated list of numbers. E.g [8, 10, 2, 4, 6]
output: an integer value to represent how many times the list was rotated. E.g 2
"""

"""Come up with some example inputs & outputs. Try to cover all edge cases.

A list of size 10 rotated 3 times.
A list of size 8 rotated 5 times.
A list that wasn't rotated at all.
A list that was rotated just once.
A list that was rotated n-1 times, where n is the size of the list.
A list that was rotated n times (do you get back the original list here?)
An empty list.
A list containing just one element.
"""

"""Come up with a correct solution for the problem. State it in plain English

# Linear Search Algorithm
Here, we iterate over the list, pick each value and check if the value is less than
the value before it, while index is still in n - 1 range, where n is the length of
the list.

STEP 1. create a variable called rotation initialized to 1
STEP 2. check if number at index rotation is less than value at index rotation - 1
STEP 3. if it does, rotation is the answer and can be returned from the function
STEP 4. if not, increment rotation by 1 and repeat STEP 2 to STEP 4
STEPN 5. if list is exhausted return 0
"""
import evaluate_test


test0 = {
    "input": {
        "data": [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    "output": 3
}

test1 = {
    "input": {
        "data": [7, 9, 11, 14, 19, 3, 5, 6]
    },
    "output": 5
}

test2 = {
    "input": {
        "data": [3, 5, 6, 7, 9, 11, 14, 19]
    },
    "output": 0
}

test3 = {
    "input": {
        "data": [19, 3, 5, 6, 7, 9, 11, 14]
    },
    "output": 1
}

test4 = {
    "input": {
        "data": [5, 6, 7, 9, 11, 14, 19, 3]
    },
    "output": 7
}

test5 = {
    "input": {
        "data": [3, 5, 6, 7, 9, 11, 14, 19]
    },
    "output": 0
}

test6 = {
    "input": {
        "data": []
    },
    "output": 0
}

test7 = {
    "input": {
        "data": [14]
    },
    "output": 0
}


tests = [test0, test1, test2, test3, test4, test5, test6, test7]


def count_rotations_linear(nums: list[int]) -> int:
    rotation: int = 1 # O(1)
    n: int = len(nums) - 1 # 0(1)

    while n > 1 and rotation <= n: # 0(N)
        
        if nums[rotation] < nums[rotation - 1]:
            return rotation # 0(1)
        
        rotation += 1 # 0(1)

    return 0 # 0(1)

for test in tests:
    evaluate_test.evaluate_test_case(count_rotations_linear, test)