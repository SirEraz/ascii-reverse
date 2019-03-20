import math

spacer = str("\n\n\n\n\n\n\n\n\n\n\n\n\n")

artLines = []
reverseLines = []

def reverse(artLines):
    return [x[::-1] for x in artLines]

print("Welcome to the ASCII Reverse tool.")
print("...")
print("Version: 1.1")
print("Author: Eraz")
print("...")
print("Press enter to begin")
enter = str(input(""))
print(spacer)

while True:
    print("How many lines long/tall is your ASCII art?")
    artHeight = int(input("Enter value: "))
    print("Ok, please paste your ASCII art line by line:*")
    print("     *include white-space!*")
    print("...\n")
    for i in range(artHeight):
        artLine = str(input(""))
        artLines.append(artLine)

    print("\n")
    for i in range(artHeight):
        revArt = reverse(artLines)
        reverseLines.append(revArt)
        print(reverseLines[i][i])

    print("")
    print("...\nPress enter to run the program again, or type anything else to exit.")
    enterP = str(input(""))

    if enterP == "":
        artLines.clear()
        reverseLines.clear()
        print(spacer)
    else:
        break


