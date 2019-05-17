username = "admin"
password = "admin"
usernameInput = input("Username :")
passwordInput = input("Password :")
if username == usernameInput and password == passwordInput:
    print("Login Done!!")
    print("---------------------------")
    print("1.VAT Calculator[THB + VAT]")
    print("2.Price Calculator [THB]")
    userselect = int(input("Pls Select >>"))
    if userselect == 1:
        price = int(input("How much your price? :"))
        vat = int(input("How much VAT(%) :"))
        result = int(price) + (int(price) * vat / 100)
        print(result)
        print("------ THX For Use VAT Calculator ------")
    elif userselect == 2:
        price1 = int(input("How Much Your Price1 : "))
        price2 = int(input("How Much Your Price2 : "))
        price3 = int(input("How Much Your Price3 : "))
        Total = (price1+price2+price3)
        print("Your total is :", Total, "THB")
else:
    print("Username or Password Incorrect Pls Fix !!!")