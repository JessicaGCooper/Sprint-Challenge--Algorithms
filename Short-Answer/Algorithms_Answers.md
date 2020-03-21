#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 
 a = 0  --> 0(1)
 while (a < n * n * n): --> this loop in theory runs n^3 times, but the n^2 below reduces it to incrementing n times --> O(n)
    a = a + n * n -->O(1)
    effectively it will increment n times

ex. n = 4
a = 0
while (a < 64):
  a = a + 16
incremented 4 times

ex. n = 20
while (a < 8000)
 a = a + 400

incremented 20 times

ANSWER: O(n)


b)
O(1)
O(n)
  O(1)
  O(n)
    0(2n)
    O(1)   

O(1)
O(n)
  O(1)
   O(n)
    O(2n)
O(1)
O(n)
  O(2n^2)

O(1) + O(2n^3)

ANSWER: O(n^3)

c)

The recursion calls itself once (about) for bunnies/n number of times
findnig the most dominant it will be O(n)

ANSWER: O(n)

## Exercise II


If you have an n-story building and dropped eggs are NOT broken on floors below floor f, but are broken are floors f and above, in order to minize the number of broken eggs while finding f AND apparantly to minizie number of dropped eggs:

A building's floors are in numerical order.  This is a sorted list.  The list can iterated over.  I must make an assumption that information on whether or not an egg will broken when dropped each floor is provided in some form. 

This could be a dictionary with key, value pairs such that:
  floors = {1: False, 2: False, 3: False, 4: True, 5: True}  
such that there are 5 floors and floor 4 is floor f.

create a function that takes in the dictionary

def find_floor(dictionary):

create a list of all values in the dictionary using the .values() method and the list method
  values = list(dictionary.values())

Find the middle value by integer division.
    mid = len(values)//2
First check mid
    if values[mid] == True:
Move left from mid until you find False
      for i in range(mid, -1):
        if values[i] == False:
          return i + 2 (i will be index of floor below floor f so add 1 to get to index floor f, than add 1 again to get floor f's true value)
    elif values[mid] == False:
Move right from mid until you find True
       for j in range(mid, len(values)-1):
        if values[j] == True
          return i + 1 (must add one to index number to accurately reflect floor number of f)

By starting in the middle you will drop the least number of eggs, and by moving right first (per condition) you will minimize breakage as well. 

Time complexity is O(1) for using the .values() method, but O(n) for using the list() method
Then O(n) for iterating over values, since only one loop will be used depending the value of mid, that loop will be O(n)
Add --> O(2n) --> drop constant --> O(n)

Time Complexity = O(n)
      


    
