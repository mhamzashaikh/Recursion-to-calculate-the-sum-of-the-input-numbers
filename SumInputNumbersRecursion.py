def sum_rec(n): 
   if n == 0:
       return n
   else:
       return n % 10 + sum_rec(n//10)
a = int(input("Enter any numbers : "))
print("The sum is :", sum_rec(a))
