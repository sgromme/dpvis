#!/usr/bin/env python3

# This is a dynamic program to add numbers from 0 to n
# see YouTuber Andrey Grehov , but was in Go
# Find the sum of the number the 
# Recurrence relation is f(n) = f(n-1) + n



def addnumbers1_to_n_recursive(n: int) -> int:
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + addnumbers1_to_n_recursive(n - 1)


# Dynamic programming approach that was generate by GPT-4.1
def addnumbers1_to_n_dynamic(n: int) -> int:
    if n <= 0:
        return 0
    dp = [0] * (n + 1)
    #dp[1] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + i
    return dp[n]

# Dynamic programming approach from YouTuber Andrey Grehov
def addnumbers1_to_n_dynamic_andrey(n: int) -> int:
    # Base case for negative numbers
    if n < 0:
        return 0
    # Initialize a list to store sums, note that we need n+1 elements (lists start at 0) to include sum for n
    # and f(0) is initialize to 0 because the it won't be calculated because 
    
    sums = [0] * (n + 1)
    for i in range(1, n + 1):
        sums[i] = sums[i - 1] + i
    return sums[n]


if __name__ == "__main__":

    n = 5
    result = addnumbers1_to_n_recursive(n)
    print(f"(Recursive) The sum of numbers from 1 to {n} is: {result}")

    result_dynamic = addnumbers1_to_n_dynamic(n)
    print(f"(Dynamic) The sum of numbers from 1 to {n} is: {result_dynamic}")

    result_dynamic_andrey = addnumbers1_to_n_dynamic_andrey(n)
    print(f"(Dynamic Andrey) The sum of numbers from 1 to {n} is: {result_dynamic_andrey}")

    n = 0
    result = addnumbers1_to_n_recursive(n)
    print(f"(Recursive)  The sum of numbers from 1 to {n} is: {result}")

    result_dynamic = addnumbers1_to_n_dynamic(n)
    print(f"(Dynamic) The sum of numbers from 1 to {n} is: {result_dynamic}")

    result_dynamic_andrey = addnumbers1_to_n_dynamic_andrey(n)
    print(f"(Dynamic Andrey) The sum of numbers from 1 to {n} is: {result_dynamic_andrey}")


    n = -5
    result = addnumbers1_to_n_recursive(n)
    print(f"(Recursive) The sum of numbers from 1 to {n} is: {result}")

    result_dynamic = addnumbers1_to_n_dynamic(n)
    print(f"(Dynamic) The sum of numbers from 1 to {n} is: {result_dynamic}")

    result_dynamic_andrey = addnumbers1_to_n_dynamic_andrey(n)
    print(f"(Dynamic Andrey) The sum of numbers from 1 to {n} is: {result_dynamic_andrey}")
