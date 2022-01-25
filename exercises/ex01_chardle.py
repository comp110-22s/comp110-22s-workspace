"""Ex01 - Chardle- a cute step toward Wordle."""

__author__= "730473073"



word: str=input("Enter a 5-character word:")
if len(word) !=5:
    print("Error: Word must have 5 characters")
    exit()
Letter: str=input("Enter a single character:")
if len(Letter)!=1:
    print("Error: Character must be a single character")
    exit()
    
print("Searching for " + Letter + " in " +word)

amount= 0
if Letter== word[0]:
    print(Letter +" found at index 0")
    amount+=1
if Letter== word[1]:
    print(Letter +" found at index 1")
    amount+=1
if Letter== word[2]:
    print(Letter +" found at index 2")
    amount+=1
if Letter== word[3]:
    print(Letter +" found at index 3")
    amount+=1
if Letter== word[4]:
    print(Letter +" found at index 4")
    amount+=1
if amount>0:
    if amount==1:
        print("1 instance of " + Letter + " found in "+ word)
    else:
        print(str(amount)+ " instances of "+ Letter + " found in " + word)
else:
    print(" No instances of "+ Letter + " found in "+ word)

