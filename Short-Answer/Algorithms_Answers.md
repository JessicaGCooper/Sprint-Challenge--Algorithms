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
    0(2)
    O(1)   

O(1)
O(n)
  O(1)
   O(n)
    O(3)
O(1)
O(n)
  O(3n)

O(1) + O(3n^2)

ANSWER: O(n^2)

c)

The recursion calls itself once (about) for bunnies/n number of times
findnig the most dominant it will be O(n)

ANSWER: O(n)

## Exercise II


