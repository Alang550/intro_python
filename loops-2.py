for number in range(100):
  result = number ** 2
  if result % 2 != 0: # odd
      print(result, "tik")
  elif number % 2 == 0:
      print(number, "t0k")
#  print prime numbers
# print numbers in descending order
# print multiplication table

# Multiplication table (from 1 to 10) in Python

num = 12

# To take input from the user
# num = int(input("Display multiplication table of? "))

# Iterate 10 times from i = 1 to 10
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)



# Python3 code to demonstrate
# Descending Sort String Numbers
# using naive method

# initializing list
test_list = [ '4', '6', '7', '2', '1']

# printing original list
print ("The original list is : " + str(test_list))

# Descending Sort String Numbers
# numeric string sorting
for i in range(0, len(test_list)) :
	test_list[i] = int(test_list[i])
test_list.sort(reverse = True)

# printing result
print ("The resultant reverse sorted list : " + str(test_list))





# Python program to display all the prime numbers within an interval

lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)