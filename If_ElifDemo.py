print("---------------------------------")
print("---- Ticket Pricing Software ----")
print("---------------------------------")

print("Please Enter Your Age :")
Age = int(input())

if(Age<=5):
    print("Free Entry")
elif(Age>5 and Age<=18):
    print("Your Ticket Price : 900")
elif(Age>18 and Age<=40):
    print("Your Ticket Price : 1200")
else:
    print("Your Ticket Price Is 500")

