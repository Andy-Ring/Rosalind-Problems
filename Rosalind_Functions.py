# This file will contain all of the functions needed to solve the Rosalind Problems

# This is the function to solve problem ini2: Variables and Some Arithmetric

def Arithmetric(a, b):
    c = (a**2)+(b**2)
    return c

# This is the function to solve problem ini3: Strings and Lists


def SliceString(str, a, b, c, d):
    new_str = str[a:b+1] + " " + str[c:d+1]
    return new_str

# This is the function to solve problem ini4: Conditions and Loops


def SumOddInt(start, end):
    result = 0
    for x in range(start, end + 1):
        if x % 2 == 1:
            result += x
    return result

# This is the function to solve problem ini5: Working with Files


def EvenLines(file):
    outputFile = []
    with open(file, 'r') as f:
        outputFile = [line for pos, line in enumerate(
            f.readlines()) if pos % 2 == 1]

    return outputFile

    with open('C:\\Users\Andrew\\OneDrive - Baylor University\\Documents\\Git Code\\Rosalind Problems\\out.txt', 'w') as f:
        f.write(''.join([line for line in outputFile]))

# This is the function for problem ini6: Dictionaries


def CountWordOcc(str):
    wordCountDict = {}

    for word in str.split(' '):
        if word in wordCountDict:
            wordCountDict[word] += 1
        else:
            wordCountDict[word] = 1

    for key, value in wordCountDict.items():
        print(key, value)
