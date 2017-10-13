#13 Oct 2017 by Aila Simpson

import string

letters = [0] * 26
spaces = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tletter = 0

print("I will find the frequency for each letter in a piece of text.")
choice = raw_input("Would you like me to read a file or take input? ")
choice = choice.lower()

if choice == "file":
    file = raw_input("What's the file called? ")
    f = open(file, "r")
    text = f.read().upper()
else:
    rawtext = raw_input("What text do you have? ")
    text = rawtext.upper()

print text

text = text.translate(None, string.punctuation)
text = text.replace("\n", "")

print text

l = len(text)

for x in range (0,l):
    a = text[x]
    if a == " ":
        spaces+=1
    else:
        b = alphabet.index(a)
        letters[b] = letters[b] + 1
        tletter+=1

for y in range (0,len(alphabet)):
    print '%s: %d' %(alphabet[y], letters[y])
