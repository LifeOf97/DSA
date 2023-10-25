import time

def evaluate_test_case(func, test: dict) -> any:

    excpected_output = test["output"]
    
    # run the test
    start_time = time.perf_counter()
    
    actual_output = func(test["input"]["data"])

    end_time: float = time.perf_counter() - start_time

    result = "PASSED" if actual_output == excpected_output else "FAILED"


    print(F"Input: {test['input']['data']}\n")
    
    print(F"Expected Output: {excpected_output}\n")

    print(F"Actual Output: {actual_output}\n")

    print(F"Execution Time: {end_time:.6f} ms\n")

    print(F"Test Result: {result}\n")

    # print(F"({actual_output}, {result}, {end_time:.6f} ms)")
