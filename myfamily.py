#Aizhan Mamatkalykova
myfamily = ("mother", "father", "sister", "brother", "sister")

# 1
print("Type of myfamily:", type(myfamily))

# 2
print("First sister:", myfamily[2])
print("Second sister:", myfamily[4])

# 3
#Tuples are immutable, that's why we can't use append(). To show it, there is a try-except block
try:
    myfamily.append("me")
except AttributeError as e:
    print("Error:", e, "- Tuples are immutable, so we cannot append items.")

# 4
#Tuples are immutable, that's why we can't use pop(). To show it, there is a try-except block
try:
    myfamily.pop()
except AttributeError as e:
    print("Error:", e, "- Tuples are immutable, so we cannot remove items.")
