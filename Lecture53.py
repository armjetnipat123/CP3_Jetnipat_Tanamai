def VatCal(totalPrice):
    result = float(totalPrice+(totalPrice*7/100))
    return result

totalPrice = float(input("How Much Your Price? :"))
print("Total is[VAT + PRICE] :",VatCal(totalPrice))