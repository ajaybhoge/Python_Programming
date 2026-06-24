def BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream Parlour")


def main():
    BigBazar()  #Allowed
    Amul()   # Error NameError: name 'Amul' is not defined
    BigBazar.Amul() #Error  AttributeError: 'function' object has no attribute 'Amul'


if __name__ == "__main__":
    main()