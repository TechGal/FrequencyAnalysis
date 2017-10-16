#13 Oct 2017 by Aila Simpson

from __future__ import division
import string

letters = [0] * 26
frequency = [0] * 26
spaces = 0
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tletter = 0

print("I will find the frequency for each letter in a piece of text.")
inchoice = raw_input("Would you like me to read a file or take input? ")
choice = inchoice.lower()

if choice == "file" or choice == "f":
    file = raw_input("What's the file called? ")
    f = open(file, "r")
    text = f.read().upper()
else:
    rawtext = raw_input("What text do you have? ")
    text = rawtext.upper()

text = text.translate(None, string.punctuation)
text = text.replace("\n", "")

l = len(text)

for x in range (0,l):
    a = text[x]
    if a == " ":
        spaces+=1
    elif a in alphabet:
        b = alphabet.index(a)
        letters[b] = letters[b] + 1
        tletter+=1

for y in range (0,len(alphabet)):
    d = letters[y]
    if d > 0:
        e = (d / tletter) * 100
        re = str(round(e, 2)).ljust(5)
        frequency[y] = re
    else:
        frequency[y] = "0"

for k in range (0,len(alphabet)):
    l = str(letters[k])
    m = l.ljust(5)
    letters[k] = m

for z in range (0,len(alphabet)):
    print "%s: %s %s" % (alphabet[z], letters[z], frequency[z])
print "Spaces: %d" %(spaces)
print "Total letters: %d" %(tletter)
