#1 What is the average length of a password?

with open("passwords.txt", 'r') as myfile:
    lines=myfile.readlines()
    count = 0
    pwHasNum = 0
    pwLength = 0
    for x in lines:

        tempPwLength = len(x)
        pwLength = tempPwLength + pwLength
        count = count + 1

    avgLength = pwLength / count
    print("The average Length of a password is " + str("{:.2F}".format(avgLength)))

#2 What percentage of passwords contains a number?

import re

with open("passwords.txt", 'r') as myfile:
    lines=myfile.readlines()
    count = 0
    pwHasNum = 0
    for x in lines:
        if not x.startswith('#'):
            count = count + 1
            if (re.search(r'\d', x)):
                pwHasNum = pwHasNum + 1
total = pwHasNum / count
percnt = total * 100
print("The total number of passwords with numbers are " + str(pwHasNum))
print(str("{:.2F}".format(percnt)) + "% of passwords contains a number")

#3 What percentage of passwords contains a number and a mix of upper and lower case?

with open("passwords.txt", 'r') as myfile:
    lines=myfile.readlines()
    count = 0
    pwHasNumCapALowLet = 0
    for x in lines:
        if not x.startswith('#'):
            count = count + 1
            x = x.rstrip()
            #find num, cap let & lower case
            if (re.findall('[a-z]', x) and re.findall('\d', x) and re.findall('[A-Z]', x)):
                pwHasNumCapALowLet = pwHasNumCapALowLet + 1
total = pwHasNumCapALowLet / count
percnt = total * 100
print("The total number of passwords with a number, upper and lower case letters are " + str(pwHasNumCapALowLet))
print(str("{:.2F}".format(percnt)) + "% of passwords contain a number with an upper and lower case letter")


#4 What are the most common Consonant and Vowel?


vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

VowelCount = {}.fromkeys(vowels, 0) 
ConstCount = {}.fromkeys(consonants, 0)

# Count vowels in a different way 
# Using dictionary 
def Check_Vow(string, vowels): 
      
    # casefold has been used to ignore cases 
    string = string.lower()
      
    
    # To count the vowels 
    for character in string: 
        if character in VowelCount: 
            VowelCount[character] += 1    
    return VowelCount 
      
def Check_Const(string, consonants):

    string = string.lower()

    for character in string: 
        if character in ConstCount:
            ConstCount[character] += 1
    return ConstCount



with open("passwords.txt", 'r') as myfile:
    lines=myfile.readlines()
    for x in lines:
        if not x.startswith('#'):
            Check_Vow(x, vowels)
            Check_Const(x, consonants)

print(VowelCount)
print("Most common vowel: " + str(max(VowelCount, key=VowelCount.get)))
print(ConstCount)
print("Most common consonant: " + str(max(ConstCount, key=ConstCount.get)))


#5 What are the least common consonant and vowel?

print("Least common vowel: " + str(min(VowelCount, key=VowelCount.get)))
print("Lease common consonant: " + str(min(ConstCount, key=ConstCount.get)))


