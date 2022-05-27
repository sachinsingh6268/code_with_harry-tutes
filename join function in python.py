lis=["John", "Cena", "Randy" , "Orton", "Sheamus", "Khali", "Jinder Mahal"]

# to print them such that these are joined by and normal and naive method is
# for item in lis:
#     print(f"{item} and",end=" ")
#
# print("other wwe superstars")


# if we will do the same thing using join then it can be done in a single line as
a=" and ".join(lis)
print(a, "other wwe superstars")

# if we want to join them with the help of commas(,)
a=" , ".join(lis)
print(a, "other wwe superstars")