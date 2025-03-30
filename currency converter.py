def currency_converter(dollar,rate):
    rupee=dollar*rate
    return rupee
q=input("enter the amount  - ")
w=input("enter the rate - ")
print(currency_converter(float(q),float(w)))
