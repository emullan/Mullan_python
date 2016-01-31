#Mullan HW2

1.
def fib(n):                 #Takes an input n and prints fibonaccit numbers less than n
  a,b = 0,1                 #I used the function in the class notes
  
  while a<n:
    print (a,end=', ')      #Print the fibonacci number and a comma
    a,b = b,a+b
  print a                   #Print the last number
  
  
2.
def mymax(a,b):                 #Takes 2 inputs and prints the larger input
 
    
  if a >= b:                    #If they are equal it only prints one of the numbers
    print a
    
  if a<b:
    print b
    
    
3.
def max_of_three(a,b,c):        #Gives the largest of 3 numbers
  Max = a                       #Assume the first number is the max
  
  if b>a:                       #If the next number is larger, it is the max
    Max = b
    
  if c>Max:                     #If the 3rd number is larger than both, it is the max
    Max = c

  print Max
    
4.
def mylen('w'):     # w is the string input
  length=0
  for char in w:              
    length = length + 1       #Increment the length with each character in w
    
  print length
  
  
5.
def vowel('l'):    # l is the one letter input
  x=0
  if l == 'a':      #Check each vowel to see if the input is a vowel
    print 'True'    #The x's are to make this function usable in exercise 6
    x=1
    
  if l == 'e':
    print 'True'
    x=1
    
  if l == 'i':
    print 'True'
    x=1
    
  if l == 'o':
    print 'True'
    x=1
    
  if l == 'u':        
    print 'True'
    x=1
    
  if l == 'y':
    print 'Sometimes'
    
  else:
    print 'False'

6.
def translate('string'):    #string is the input string for this function
  y=0
  z=len(string)   # sets up a comparison point for i know when to stop my loop
  
  while y<z:             #Makes sure we stop at the end of the string
    vowel(string[y])    #Uses the function vowel from problem 5 to see if the character is a vowel. If x=0, the character is a consonant
    
    if x=0:
      string = string[:y] + 'o' + string[y] + string[y+1:]    #string is now the string with the new letters inserted
      y=y+3                                                   #Increment y by 3 to skip over the characters I just inserted
      z=len(string)                                           #Reset the new string length for comparison in the while loop
      
    else:
      y=y+1                                                   #If the character is a vowel, increment y and check the next index
      
  print string                                                #After the while loop
  
7.
def sum(list):      #The input is a list of numbers
  
  sum = 0
  x=0
  y=len(list)   #Set up a counter to make sure I stop adding at the end of the list
  
  while x<y:
    sum = sum + list[x]
    x = x+1
    
  print sum
  
def multiply(list):  #The input is a list of numbers
  product = 1
  x=0
  y=len(list)   #Set up a counter to make sure I stop adding at the end of the list
  
  while x<y:
    product = product * list[x]
    x = x+1
    
  print product
  
8.
def reverse(string):
  y = len(string)-1         #Establish y as the index to pull characters from string
  newstring = ''            #Establish the output newstring as an empty string to put characters into
  
  while y>=0:
    newstring = newstring + string[y]     #Insert characters into newstring starting with the last character in string
    y=y-1
    
  print newstring
  
9.
def is_palindrome(string):
  reverse(string)                 #Use the reverse function from the previous exercise
  
  if string==newstring:
    print 'True'
    
  else:
    print 'False'
    
10.
def is_member(x,a):   #function to find if x is in a
  z=0
  y = len(a)
  s=0                   #If s is positive, then there is an x in a
  
  while z<y:
  
    if x==a[z]:       #Check each index of a for x
      s = s+1         #increment s if a is in x
      z=z+1
      
    else:
      z=z+1         
      
  if s>0:
    print 'true'
    
  else:
    print 'false'
      
      
11.
def overlapping(a,b):

  s=0                 #If s is positive, they have a member in common
  
 for chara in a:      #Nested for loop that combines to check every pairing of a and b
 
  for charb in b:
  
    if chara==charb:  #Increments the counter if there is a match
      s=s+1
      
  if s>0              #If the counter has been incremented at all, there is a match
    print 'True'
    
  else:
    print 'False'
    
    
12.
def generate_n_chars(n,c):    #n is a number and c is a character
  s=0
  string = ''
  
  while s<n
    string = string + c       #attach another character c to the end of the string until we have the number we need
    s = s+1
    
  print string
    
  
## Test cases

print('#1\n')
fib(500)
print('\n')

print('#2\n')
print(mymax(45,987), '\n')

print('#3\n')
print(max_of_three(3,4,5),'\n')

print('#4\n')
print(mylen('Gerhard'))
print(mylen([1,2,3,4,5,6,7]))
print('\n')

print('#5\n')
print(vowel('e'))
print(vowel('H'))
print('\n')

print('#6\n')
print(translate("this is fun"))
print(translate('aeiou'))
print(translate('YYYYYYY'))
print(translate("mmmmmm"))
print('\n')

print('#7\n')
print(sum([1,2,3,4,5]))
print('\n')

print('#8\n')
print(multiply([0,1,2,3]))
print(multiply([1,2,3,4]))
print('\n')

print('#9\n')
print(reverse("gnitset ma I"))
print('\n')

print('#10\n')
print(is_palindrome('radar'))
print(is_palindrome('Gerhard'))
print('\n')

print('#11\n')
print(is_member('dog', ['cat', 'dog', 'zebra']))
print(is_member(3, [1,2,3,4]))
print(is_member(3, [5,6,7]))
print('\n')

print('#12\n')
print(overlapping([1,2,3], [3,4,5]))
print(overlapping([1,2,3], [6,4,5]))
print('\n')

print('#13\n')
print(generate_n_chars(7, 'g'))
  
