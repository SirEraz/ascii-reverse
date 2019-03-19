import math

spacer = str("\n\n\n\n\n\n\n\n\n\n\n\n\n")

artLines = []

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
    print("Ok, please paste your ASCII art line by line:")
    print("...\n")
    for i in range(artHeight):
        artLine = str(input(""))
        artLines.append(artLine)

    for i in artHeight:
        revArt = artLines[i][::-1]
        print("{}".format(artLines))

    print("")
    print("...\nPress enter to run the program again, or type anything else to exit.")
    enterP = str(input(""))

    if enterP == "":
        break
    else:
        exit()
