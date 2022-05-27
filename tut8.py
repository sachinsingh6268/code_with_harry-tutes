name="my name is Sachin Singh"
print(len(name))
print(name[:6:23423])
check=name.endswith("Singh")
print(check)
print(name.count('nS'))
print(name.capitalize())
print(name.find("San"))
print(name.lower())
print(name.upper())
print(name.replace("is","is not"))
# we can also first replace and then print as
name=name.replace("my name is","I am")
print(name)