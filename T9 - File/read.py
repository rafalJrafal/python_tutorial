#https://www.w3schools.com/python/python_file_open.asp

file = open("demoFile.txt")
print(file.read())
file.close()

file = open("demoFile.txt")
print(file.read(3))
file.close()

file = open("demoFile.txt")
print(file.readline())
file.close()

for line in open("demoFile.txt"):
    print(line.strip())