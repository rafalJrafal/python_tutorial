# https://www.w3schools.com/python/python_strings.asp

str = """a happy
multiline bshit"""

print(str)

print(str[10])

for character in str:
    print(character)

print("length: ", len(str))

print("shit" in str)
print("shit" not in str)
print("aaa" not in str)
print("aaa" in str)

print(str[2:10])
print(str[:10])

print(str.upper())
print(str.upper().lower())

print(str.replace("bshit", "bullshit!!!"))

print(str.split("\n"))

age = 50
number = 22
print(f"my age is {age} and my number is {number:.2f}")
print(f"number {age} multiplied by {number} is {age*number}")

str = "we are \"vikings\""
print(str)