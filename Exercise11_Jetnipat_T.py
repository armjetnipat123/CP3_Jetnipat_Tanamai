Number = int(input("User Number Select :"))
text = input("Select icon do you want :")
for i in range(Number):
    print(" "*(Number-(i+1))+(text*(i+1))+(text*i))