# Backstory: Usain Bolt, you, and Aybek
# had a race. Surprisingly, Usain bolt won.
# You came in 2nd and Aybek came in 3rd :(.
# Can you think of a way to write a function
# that given a person's name, returns his/her place?
# ALSO
# Can you think of a way to write a function
# that given a place, returns his/her name?
a=input("Enter the name or place of the marathon participant:")
if a==1:
	print("Usain Bolt")
elif a=="Usain Bolt":
	print("1")
elif a==2:
	print("Avtandil")
elif a=="Avtandil":
	print("2")
elif a==3:
	print("Aibek")
elif a=="Aibek":
	print("3")
else: 
	print("There is no such member in our data!")
