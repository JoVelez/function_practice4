import math

#function max_num to find highest number

def max_num(a,b,c):
 return max(a,b,c)

print(max_num(5,45,12))

#mult_list() to multiply nums in list
#can use .prod here

math.prod([1, 2, 3, 4,])

#rev_string() to reverse string
#w3 schools, creates a slice that moves backwards

def rev_string(x):
  return x[::-1]

mytxt = rev_string("I wonder how this text looks like backwards")

print(mytxt)


#num_within() to check range
#solution answer
#range() a possible option
def num_within(x,a,b):
  return x in range(a,b+1)
       
print(num_within(10,2,5))

#solution code, couldn't quite figure this one out

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)