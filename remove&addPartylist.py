#8.2.3 Add a new name to the party list.

   # add a new name
   if choice == "a":
       newName = raw_input("\nEnter a name to add to the party list: ")
       names.append(newName)

#8.2.4 Remove a new name from the party list.


   # remove a name
   elif choice == "b":
        oldName = raw_input("\nEnter the name you wish to remove: ")
        if oldName in names:
            names.remove(oldName)
        else:
            print oldName,"is not in the party list."
