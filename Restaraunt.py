#This is a restraunt where you can order steaks, fries and drinks
print("Thank you for coming in today!!. This is Jackers Restaurant")

#this asks for the users name
name  = input ("what is your name? ")

#an if statement that if the users name is hacker the user is asked if they are evil if yes the user is not welcomed into the restraunt else if they are not named hacker are allowed to go in. also if tou choocse no when asked if you are evil you can proceed
if name == "hacker":
  evil_status = input ("Are you evil?")
  if evil_status == "yes":
    print("You are not welcome here")
    exit()
   
  else: 
    print ("Glad you are not one of the evil ones")



else: 
  print ("Hello " + name + ", its great having you here what would you like to order\n" )
  
#this asks you what you would like to order
print ("- We have a variable of options\n" + "steaks\n" + "fries\n" + "drinks\n" )

#this assigns order as your input
order = input ()

#if or else statement that if a user chooses steak then the price is 20 dollars elseif (elif) the user chooses fries the price is 20. if the user gives an input that is not offered they are asked if they want something else if yes then its looped back to ask for what they want if not exits
if order == "steaks":
  price = 20
elif order == "fries":
  price = 10
elif order == "drinks":
  price = 5
else:
  print ("sorry we dont have that here!")
  no_order = input("would you like to order something else?")
  if no_order == "yes":
    print ("- We have a variable of options\n" + "steaks\n" + "fries\n" +    "drinks\n")
    order = input ()

    if order == "steaks":
      price = 20
    elif order == "fries":
      price = 10
    elif order == "drinks":
      price = 5
  else:
    print ("Have a nice day!!")
    exit()

#asks for the quantity user wants
quantity = input("I see you got friends, for how many people? ")

#if user wants ketchup they can order tbat too
ketchup = input ("would you guys like some ketchup with your order? ")
if ketchup == "yes":
  ketchup = 2


#multiplies the price by quantity
total = (price * int(quantity)) + (int(ketchup) * int(quantity) )

print("Thank you your total is : $" + str(total))

print ("Great " + name + ", we would get " + quantity + " " + order + " ready for you in a second, pls get seated")
