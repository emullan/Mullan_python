#Mullan_HW3

## Need to use docstrings for function headers

#1. Histogram
def histogram(list):
    for int in list:                    #Check every integer in the list               
        y=int                           # establish comparison between the number and counter
        x=0
        string = ''
        while x<y:
            string = string + '*'       #add an asterisk for every time through the loop
            x=x+1
            
        print (string)                  #Print the string after each while loop is complete
        
#2. maximum in a list
def max_in_list(list):
    x=1                             
    y=len(list)
    max=list[0]                         #assume the 1st one is the max
    
    while x<y:                          #While we are going through the list
        if list[x]>max:                 #Set a new max if the one we're checking is bigger than the current max
            max=list[x]
            x=x+1
        else:
            x=x+1
    print (max)
    
#3. Lengths of words
def listofwords(words):     #words must be a list of strings in brackets. For example: ['Hoya','Saxa','Jack']
    numberlist = []         #Blank list to put lengths in  
    x=0                     #counter for the position in the input words
    for string in words:
        numberlist.append(len(words[x]))    #Places the len of the string in the list   
        x=x+1                               #Increase the counter to get the length of the next string
    return (numberlist)

#4. Find longest word
def find_longest_word(words):           #words must be a list of strings in brackets
    longest = words[0]                  #assume the first one is the longest
    x=0                                 #Counter
    for string in words:
        if len(words[x])>len(longest):  #if the string that we are looking at is longer than the previous longest word,
            longest = words[x]          #It is the new longest word
        
        x=x+1                           #Increase the counter to check the next word in the list
                
    return len(longest)                 #Return the length of the longest word

#5. Filter long words
def filter_long_words(words,n):
    longwords = []                      #Create an empty list to put my words in if they fit criteria
    for string in words:                #Check every string in the list
        if len(string)>n:               #Add the string to the empty list longwords if it is long enough
            longwords.append(string)
            
    return longwords
    
#6. advanced palindromes
from string import punctuation
def strip_string(s):                #This function converts capital case to lower case and strips punctuation and blank spaces
    
    new=list(s)                     #Converts the string s to a list and replaces spaces with nothing
    x=0
    for char in new:
        if new[x]==' ':
            new[x]=''
        
        x=x+1
    d = ''.join(new)                #Joins the list into a string d
    d=d.lower()                     #Converts upper case letters in string d to lower case
    return ''.join(c for c in d if c not in punctuation)    #removes punctuation

def reverse(string):        #Gets the palindrome of a string
  y = len(string)-1         #Establish y as the index to pull characters from string
  newstring = ''            #Establish the output newstring as an empty string to put characters into
  
  while y>=0:
    newstring = newstring + string[y]     #Insert characters into newstring starting with the last character in string
    y=y-1
    
  return (newstring)

def is_palindrome(string):
    stripped=strip_string(string)                   #Use the strip_string function to remove punctuation and spaces
    newstring = reverse(stripped)                 #Use the reverse function to get the palindrome of the stripped string
  
    if stripped==newstring:                         #compare the stripped string to its palindrome
            return True
    
    else:
            return False
            
#7. Pangrams
def pangram(string):
    string=string.lower()                               #Change it to all lower case to check
    if ('a' in string) and ('b' in string) and ('c' in string) and ('d' in string) and ('e' in string) and ('f' in string) and ('g' in string) and ('h' in string) and ('i' in string) and ('j' in string) and ('k' in string) and ('l' in string) and ('m' in string) and ('n' in string) and ('o' in string) and ('p' in string) and ('q' in string) and ('r' in string) and ('s' in string) and ('t' in string) and ('u' in string) and ('v' in string) and ('w' in string) and ('x' in string) and ('y' in string) and ('z' in string):
        return True                                     #Returns true if it has all 26 lower case letters
    else:
        return False
        
#8. Coke on the wall
def lyrics():
    x=9                                                #start count at 99 and decrease until it is at 1
    while x>0:
        print (x , ' bottles of coke on the wall, ' , x , 'bottles of coke. \nTake one down, pass it around, ' , x-1 , ' bottles of coke on the wall.')
        x=x-1
        
#9. English to swedish translator
## Only returns a single word instead of building a list of words - Prof G
def translate(list):                    #Input must be a list of strings. Won't work if you input a string that is not in the dictionary
    d={'merry':'god','christmas':'jul','and':'och','happy':'got','new':'nytt','year':'ar'}
    for word in list:
        word=d[word]                    #Translate each word in the list according to the dictionary
        return word
        
#10. Character Frequency counter
def char_freq(string):
    lis=list(string)                        #Turn the string into a list
    d = {x:lis.count(x) for x in lis}       #Create a dictionary mapping the character to the count for each character
    return d                                #Return the dictionary

#11. Caesar Cypher
def cypher(string):
    key={'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m','A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'}
    lis=list(string)                        #Break the string down to a list of characters
    x=0
    for char in lis:                        #Run through each character in the list
        if char in key:                     #Check to make sure the character is in the dictionary (exclude punctuation and spaces)
            lis[x]=key[lis[x]]              #Replace the character with the corresponding cipher key
        x=x+1
    s=''.join(lis)                          #Join the characters back to a string s
    return s

#12. Correct spacing issues
def correct(string):
    lis=list(string)                                    #turn the string into a list
    x=0                         
    for char in lis:
        if (lis[x] == ' ') and (lis[x+1]==' '):         #If there are 2 straight spaces, delete the first space
            lis[x]=''
        if (lis[x]=='.') and (lis[x+1]!=' '):           #If there is no space after a period, insert a space
            lis.insert(x+1, ' ')
        x=x+1
    s=''.join(lis)                                      #Join the list back into a string
    return s
    
#13. Create 3rd person singular form of verbs
def make_3sg_form(verb):
    tup=('o','ch','s','sh','x','z')                 #Create a tuple to account for multiple possibilities
    if verb.endswith('y'):                          #If the verb ends in y, drop the y and add ies to the end of the verb
        verb= verb[:len(verb)-1]+'ies'
        return verb                                 #Return statement must be within the if statement so it doesnt add an extra ending in the next step
    if verb.endswith(tup):                          #If the verb ends with something in the tuple, add es to the end of the verb
        verb=verb + 'es'
        return verb
    else:                                           #otherwise, jut add s to the end of the verb
        verb=verb+'s'
        return verb

#14. present participle generator
def make_ing_form(verb):
    vowels=['a','e','i','o','u']                        #Create list of vowels to reference
    exceptions=['be','see','flee','knee']               #Establish some of the exceptions to the first rule
    lis=list(verb)                                      #make a list of letters in verb to reference
    if verb.endswith('e') and verb not in exceptions and lis[len(lis)-2]!='i':  #Verbs that arent exceptions and end in e
        verb=verb[:len(verb)-1]+'ing'
        return verb
    if verb.endswith('ie'):                             #verbs that end in ie
        verb=verb[:len(verb)-2]+'ying'
        return verb
    if verb[len(verb)-3] not in vowels and verb[len(verb)-2] in vowels and verb[len(verb)-1] not in vowels:     #Verbs that end in cons-vowel-cons
        verb=verb+verb[len(verb)-1]+'ing'
        return verb
    else:
        verb=verb+'ing'
        return verb                                     #Return statement under each condition so it doesnt add extra endings

##Test Cases
help(histogram)
help(make_ing_form)

print("1 Histogram ", histogram([1,2,3,5,6,7,6,5,4,3,2,1]), '\n')

print("2 Max in List 77 ", max_in_list([1,2,3,77,4,5,6,7]), '\n')

print("3 word to length map 3,5,7,4 ", listofwords(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("4 Longest word 7 ", find_longest_word(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("5 filter long words snake, dolphin ", filter_long_words(['dog', 'snake', 'dolphin', 'cats'],4), '\n')

print("6 Palindrome phrase TRUE ", is_palindrome("Go hang a salami I'm a lasagna hog."), '\n')

print("7 Pangram TRUE ", pangram("The quick brown fox jumps over the lazy dog."), '\n')

print("8 Cokes \n", lyrics())

print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate(['merry', 'christmas', 'happy']), '\n')

print("10 Char Freq {'a': 7, 'c': 3, 'b': 14, 'e': 2, 'd': 3, 'g': 7, 'f': 3} ", char_freq("agbbabgcbdbabdgbdbabageebabcbgcbffgfabg"), '\n')

print("11 Decoder Caesar cipher? I much prefer Caesar salad!", cypher("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"), '\n')

print("12 correct This is very funny and cool. Indeed!", correct("This is very funny and cool.Indeed!"), '\n')

print("13 3ps brushes ", make_3sg_form("brush"), '\n')
print("13 3ps tries ", make_3sg_form("try"), '\n')
print("13 3ps runs ", make_3sg_form("run"), '\n')
print("13 3ps fixes ", make_3sg_form("fix"), '\n')

print("14 ing lying ", make_ing_form("lie"), '\n')
print("14 ing seeing ", make_ing_form("see"), '\n')
print("14 ing moving ", make_ing_form("move"), '\n')
print("14 ing hugging ", make_ing_form("hug"), '\n')