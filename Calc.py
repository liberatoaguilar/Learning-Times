def Calculato():
    equ = input("Multiply, Divide, Add, Subtract, or Other? ")
    num = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    if equ == "Multiply":
        mdas = num * num2
    elif equ == "Divide":
        mdas = num / num2
    elif equ == "Add":
        mdas = num + num2
    elif equ == "Subtract":
        mdas = num - num2
    elif equ == "Other":
        ask = input("What would you like to do? PERCENT CALC, BINARY CONVERTER ")
        if ask == "Percent Calc":
            ask1 = input("Percent increase/decrease or Percent off? ")
            if ask1 == "Percent increase/decrease":
                if num > num2:
                    decrease = num - num2
                    mdas = (decrease / float(num)) * 100
                elif num < num2:
                    increase = num2 - num
                    mdas = (increase / float(num)) * 100
            elif ask1 == "Percent off":
                percent = (100 - float(num2)) / 100
                mdas = float(num) * percent
        elif ask == "Binary Converter":
            import binary
    print("The answer is: %s" % (mdas))
Calculato()
again = input("Run Again? ")
if again == "Yes":
    Calculato()
elif again == "No":
    False
elif again == "No, thank you":
    print("I appreciate your manners.")
else:
    False
