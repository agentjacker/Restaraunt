#making a list in python
#restraunt_utensils = "spoon, fork, frying pan, pot, oven, dishwasher"

#print (restraunt_utensils)

supplies = ["spoon", "fork", "frying pan", "pot", "oven", "dishwasher"]

#i just assigned values to the list 
restraunt_list = ["spoon" , "fork" , 30 , 22.9 , True]

#me = restraunt_utensils[0]
#when you use a -in a list it basically starts from the back and counts.. so the last thing in the list would be given the value -1 second to last would be -2
#you = restraunt_utensils[-2]
#print (me)
#print (you)

#append is a method to add things to our list
#supplies.append("toilet paper")
#supplies.append("bidet")

#extend allows you to add more than one item to a list it needs  to be ([data])
#supplies.extend(["toilet paper" , "bidet"])

supplies.insert(0,"bidet")
supplies.insert(-1,"toilet paper")

#the clear method is used to delete a list completely
#supplies.clear()
#the remove method is used to remove a specific object in a list 
#supplies.remove ("spoon")
print("this item was just deleted " + supplies.pop(0))
#print(supplies.pop(0))
print (supplies)
