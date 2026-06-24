
def main():
    print("Enter First number")
    Value1 = int(input())

    print("Enter Second number")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)
    print("Addition is: " ,Ret)   # Error perform because module was not defined

if __name__ == "__main__":
    main()
