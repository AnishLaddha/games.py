##Hangman game
import random
import sys
words = ["Hello", "Python", "Computers", "Hangman", "Anish"]
word = words[random.randint(0,len(words)-1)]
print(word)
length = len(word)
wordList = list(word)
reveal = []
correct = []
i = 0
while i <= length:
    reveal.append('_')
    i = i +1
print(reveal)
def guess():
    x= raw_input("Guess Letter: ")
    a = 0
    correct = []
    for char in wordList:
        if char == x:
            correct.append(a)
            a=a+1
    return correct
def revealUpdate(correctList):
    if len(correctList) != 0:
        for yes in correctList:
            yesLetter = wordList[yes]
            reveal[yes] = yesLet
    print(reveal)
def continueGame():
    c = 0
    for r in reveal:
        if r != '_':
            c = c+1
    if c == length:
        print("you win")
        sys.exit()
    else:
        guess()
        revealUpdate(correct)
        continueGame()
continueGame()

