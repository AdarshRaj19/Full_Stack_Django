"""n=int(input("Enter the number : "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if col>=row and col<=n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
"""

""""
n = int(input("Enter the number : "))
for row in range(1, n+1):
    for col in range(1, n+1):
        if col >= n - row + 1:   
            print(col, end=" ")
        else:
            print(" ", end=" ")
    print()
"""
"""
n = 4
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for num in range(n - row + 1, n + 1):
        print(num, end=" ")
    print()
"""
"""  
   4 
  3 4
 2 3 4
1 2 3 4
"""
"""
n=int(input("Enter the number : "))
for row in range(1,n+1):
    for col in range(1,2*n):
        if row!=n and col>=row+1 and col<=(2*n)-row-1:
            print(" ",end="")
        else:
            print("*",end="")
    print()
"""

"""
*     *
**   **
*** ***
*******
"""
"""
n = int(input("Enter the number: "))
for row in range(n, 0, -1):  
    for col in range(1, 2*n):
        if row != n and col > row and col < (2*n) - row:
            print(" ", end="")
        else:
            print("*", end="")
    print()
"""

"""
*********
**** ****
***   ***
**     **
*       *
"""
"""
n = 5
# Upper half (including middle line)
for row in range(n):
    for col in range(n - row):
        print("*", end="")
    for space in range(row * 2 - 1):
        print(" ", end="")
    if row != 0:
        for col in range(n - row):
            print("*", end="")
    else:
        for col in range(n - row - 1):
            print("*", end="")
    print()

# Lower half (excluding middle line)
for row in range(2, n + 1):
    for col in range(row):
        print("*", end="")
    for space in range((n - row) * 2 - 1):
        print(" ", end="")
    if row != n:
        for col in range(row):
            print("*", end="")
    else:
        for col in range(row - 1):
            print("*", end="")
    print()
"""

"""
*********
**** ****
***   ***
**     **
*       *
**     **
***   ***
**** ****
*********
"""

"""
n = int(input("Enter the number of rows: "))
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row == 1 or row == n or col == n - row + 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
"""
"""
****
  *
 *
****
"""

