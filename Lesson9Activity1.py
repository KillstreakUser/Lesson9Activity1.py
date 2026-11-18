n = int(input("How Many Characters to Preview???"))
file = open("C:\\Users\\ajayk\\OneDrive\\Documents\\Codingul Codes\\Codingal Activities\\Module.8\\ClassNotes.txt", "r")
print(file.read(n))
file.close()
print()

file = open("C:\\Users\\ajayk\\OneDrive\\Documents\\Codingul Codes\\Codingal Activities\\Module.8\\ClassNotes.txt", "r")
lines = file.readlines()
file.close()
print("Total Lines :", len(lines))
for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())
print()

word = input("Skip Lines staring with: ")
file = open("C:\\Users\\ajayk\\OneDrive\\Documents\\Codingul Codes\\Codingal Activities\\Module.8\\ClassNotes.txt", "r")
for line in file:
    if line.startswith(word):
        print("Skip ->", line.strip())
    else:
        print("Keep ->", line.strip())
file.close()
print()

file = open("C:\\Users\\ajayk\\OneDrive\\Documents\\Codingul Codes\\Codingal Activities\\Module.8\\ClassNotes.txt", "r")
lines = file.readlines()
file.close()
out = open("Odd-Lines.txt", "w")
for i in range(0, len(lines), 2):
    out.write(lines[i])
out.close()
print("Odd Lines saved to Odd-Lines.txt")