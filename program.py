import sys


def divide(num,den):
    try:
        res=num/den
        return res
    except ZeroDivisionError:
        print("Divide fun")
        raise TypeError

try:
    num = int(input("Enter the numerator"))
    den = int(input("Enter the numerator"))

    result=divide(num,den)
    print("REs",result)
    sys.exit(-1)


except ValueError:
    print("value")

finally:
    print("finally block")

print("EOF")
