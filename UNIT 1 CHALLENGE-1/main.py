def fact_prog(n):
  if n == 1 or n == 0:
    return 1
  else:
    return n * fact_prog(n - 1)


number = int(input("Enter a value :"))
res = fact_prog(number)
print("The factorial of ", number, "is", res)
