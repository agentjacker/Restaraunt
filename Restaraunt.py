print("Thank you for coming in today!!. This is Jackers Restaurant")

name  = input ("what is your name? ")

print ("Hello " + name + ", its great having you here what would you like to order\n" )

print ("- We have a variable of options\n" + "steaks\n" + "fries\n" )

order = input ()

price = 8

quantity = input("I see you got friends, for how many people? ")

total = price * int(quantity)

print("Thank you your total is : $" + str(total))

print ("Great " + name + ", we would get " + quantity + " " + order + " ready for you in a second, pls get seated")
