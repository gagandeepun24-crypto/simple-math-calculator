print("WELCOME TO BASIC MATH CALCULATOR!!!")
print("1.ADDITION!!!")
print("2.SUBSTRACTION!!!")
print("3.MULTIPLICATION!!!")
print("4.DIVISION!!!")
print("5.MODULUS!!!")
print("6.SIN(X) value!!!")
print("7.POWER!!!")
def operation(choice):
    match choice:
        case 1:
            print("ADDITION!!!")
            a=int(input("enter first value:"))
            b=int(input("enter second value:"))
            print("Addition of two numbers is:",a+b)

        case 2:
            print("SUBSTRACTION!!!")
            a=int(input("enter first value:"))
            b=int(input("enter second value:"))
            print("Substraction of two numbers is:",a-b)
        
        case 3:
            print("MULTIPLICATION!!!")
            a=int(input("enter first value:"))
            b=int(input("enter second value:"))
            print("Multiplication of two numbers is:",a*b)

        case 4:
            print("DIVISION!!!")
            a=int(input("enter first value:"))
            b=int(input("enter second value:"))
            if a==0 or b==0:
                print("ERROR in division ( no number can be divided by 0)...")
            else:
                print("Division of two numbers is:",a/b)
        case 5:
            print("FINDING REMAINDER!!!")
            a=int(input("enter first value:"))
            b=int(input("enter second value:"))
            if a==0 or b==0:
                print("ERROR in division ( no number can be divided by 0)...,hence modulus is not found")
            else:
                print("Modulus of two numbers is:",a%b)
        case 6:
            print("sin(x) value!!!")
            import math
            angle=float(input("enter value of x (ANGLE IN DEGREES):"))
            radians=math.radians(angle)
            print(math.sin(radians))
        case 7:
            print("POWER OF NUMBER!!!")
            a=int(input("enter first value(base):"))
            b=int(input("enter second value(power):"))
            print("power:",a**b)

        case _:
            print("INVALID CHOICE???")
    return "THANK YOU ^_^"


choice=int(input("### ENTER WHICH OPERATION U WANT TO PERFORM ###:\n"))
print(operation(choice))

                



