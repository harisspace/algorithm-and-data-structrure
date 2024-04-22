# Example case fibonacci number
# f(n) = f(n - 1) + f(n - 2)
# Where f(1) = 1 and f(0) = 0 -> as base case

# O(2^n) time complexity (upper bound)
def fib(n):
  if n <= 1:
    return n
  return fib(n - 1) + fib(n - 2)