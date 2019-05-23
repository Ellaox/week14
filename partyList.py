# partyList.py 
# a program to introduce list methods
# to maintain a list of names to invite
# to a party.
# D.H. March 2005

print "\t\tThis program allows you to maintain"
print "\t\ta list of names of people to invite"
print "\t\tto a party\n"

names = []   # create an empty list

choice = "z" # initialize choice with any value that will
             # set the while loop to true

while choice != "q":
   print """
   Choose what you would like to do from the following menu (or q to exit)"

   a: Add a name

   b: Remove a name 

   c: Display the names invited

   d: Sort the names alphabetically
   
   e: Display the number of people invited

   q: Quit the program

   """
   # Get user choice

   choice = raw_input("\nType in your choice(a,b,c,d,e (or q to exit): ")
   
   # add a new name
   if choice == "a":
       newName = raw_input("\nEnter a name to add to the party list: ")
       names.append(newName)
       
   # remove a name
   elif choice == "b":
        oldName = raw_input("\nEnter the name you wish to remove: ")
        if oldName in names:
            names.remove(oldName)
        else:
            print
            print oldName,"is not in the party list."
            
   # display those invited   
   elif choice == "c":
       print "\nYou have invited "
       for i in names:
           print i
           
   # sort the names alphabetically
   elif choice == "d":
       names.sort()
       
   # use the function len to calculate the number of people invited
   elif choice == "e":
       numberOfPeople = len(names)
       if numberOfPeople == 0:
           print "\nYou have not invited anybody"
       elif numberOfPeople == 1:
           print "\nYou have invited", numberOfPeople,"person"
       else:
           print "\nYou have invited", numberOfPeople,"people"
   
   # quit the program or invalid input
   elif choice == "q":
       print "\nGoodbye!"
   else: # if user chose anything other than a – e, or q
       print "\n Sorry, there was an error in your input"
       print " Valid choices are a,b,c,d or e"
       print " to quit: type q" 
       
       
       ==================================================================================
       
       
       Python 2.7.6 (default, Nov 10 2013, 19:24:24) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
		This program allows you to maintain
		a list of names of people to invite
		to a party


   Choose what you would like to do from the following menu (or q to exit)"

   a: Add a name

   b: Remove a name 

   c: Display the names invited

   d: Sort the names alphabetically
   
   e: Display the number of people invited

   q: Quit the program

   

Type in your choice(a,b,c,d,e (or q to exit): b

Enter the name you wish to remove: Dan

Dan is not in the party list.

   Choose what you would like to do from the following menu (or q to exit)"

   a: Add a name

   b: Remove a name 

   c: Display the names invited

   d: Sort the names alphabetically
   
   e: Display the number of people invited

   q: Quit the program

   

Type in your choice(a,b,c,d,e (or q to exit): q

Goodbye!
>>> 
       
