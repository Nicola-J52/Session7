s = "hello"
useful_methods = [m for m in dir(s) if "__" not in m]
print(useful_methods)

print(help(s.capitalize))
print(s.capitalize())

print("HELLO".casefold()) # same as .lower() method

print("hello".center(50))
print("hello".center(50,"X"))

print("I see a little dove".count("e")) # how many times to I see "e"
print("banananananananana".count("ana"))
x = "I do not cook not compare"
print(f"There are {x.count("o")}os inside: '{x}'")
print("helooo00000ooollolo".find("l", 10))

s = "bob goes home to meet bob so they can take their bob and go bobing"
pos = 0 