print("--------------- Welcome ---------------")
username = "Musical"
password = "Musician"
usernameInput = input("Username :")
passwordInput = input("Password :")
if username == usernameInput and password == passwordInput:
    print("   ")
    print("---- Which Price You Looking For -----")
    print("Welcome :",usernameInput,"Which Price You Been Looking For?")
    print("1.Guitar    : 5000   THB")
    print("2.Bass      : 6500   THB")
    print("3.Keyboard  : 15000  THB")
    print("4.Violine   : 20000  THB")
    print("5.Drum      : 30000  THB")
    userselect = int(input("Pls Select Your Option >>"))
    if userselect == 1:
        Music1 = int(input("How Much Do You Want Guitars? :"))
        Price1 = 5000
        print("   ")
        print("You Bought", Music1,"Guitars", "Total is :", Music1 * Price1, "THB")
        print("--------------- Thx For Use Our Shop ---------------")
    if userselect == 2:
        Music2 = int(input("How Much Do You Want Bass? :"))
        Price2 = 6500
        print("   ")
        print("You Bought", Music2, "Bass", "Total is :", Music2 * Price2, "THB")
        print("--------------- Thx For Use Our Shop ---------------")
    if userselect == 3:
        Music3 = int(input("How Much Do You Want Bass? :"))
        Price3 = 6500
        print("   ")
        print("You Bought", Music3, "Keyboard", "Total is :", Music3 * Price3, "THB")
        print("--------------- Thx For Use Our Shop ---------------")
    if userselect == 4:
        Music4 = int(input("How Much Do You Want Violine? :"))
        Price4 = 20000
        print("   ")
        print("You Bought", Music4, "Violine", "Total is :", Music4 * Price4, "THB")
        print("--------------- Thx For Use Our Shop ---------------")
    if userselect == 5:
        Music5 = int(input("How Much Do You Want Drum? :"))
        Price5 = 30000
        print("   ")
        print("You Bought", Music5, "Drum", "Total is :", Music5 * Price5, "THB")
        print("--------------- Thx For Use Our Shop ---------------")
else:
    print("Pls check your username or password!!")