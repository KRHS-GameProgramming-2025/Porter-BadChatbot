name = input("what is your name? ")
greeting = "hello" 
goodbye = "bye"
print (greeting  + " " + name) 

colors = ["red",
		  "green",
		  "blue",
		  "purple",
		  "yellow",]
		  

color = input("what is your least favorite  color?  ")
if color == "brown" or color == "Brown":
	print("brown is a horrible color")
elif color.lower() in colors:
	print(color.capitalize() + " is my favorite color. "+ color.capitalize()+  " is amazing") 
else:
	print("I do not know " + color)


fallsport = input("what is your favorite fall sport? ")
if fallsport.lower() == "football":
	print(fallsport.lower() + " is mine too " + name)
else:
	Sport2 = input ("I dont know that sport " + name + " how do you play the sport? " + name+"." )
	print ("thats sounds fun , but complicated")
 
	


food= input("whats your favorite food? " + name + " ")
if food == "sushi" or food == "Sushi":
	print("cool that's my favorite food")
else :
	food2 = input ("I dont know that food whats it made of? ")
	


	
	
cook = input ("is " + food +" hard to make? ")
if cook == "yes":
	print("I bet it is hard")
elif cook == "no":
	print("oh it sounded hard")
else:
	print (" use yes or no" ) 
print (":)")
	
	

