# Barbara King
# HW 8-5: inventory.py
#
#   Starting code for a simple inventory tracking program using
#       dictionaries.
#

def getCommand():
    command = input("Enter command: ")
    return command

def addToInventory(dict, inventory):

    for item in dict:
        # if item in inventory.keys():
        #     inventory[item] += dict[item]
        # else:
        #     print(dict)
        #     inventory[item] = dict[item]
        inventory[item] = inventory.get(item,0) + dict[item]
    # print(inventory)
    return inventory

def viewInventory(dict):
    for (k,v) in dict.items():
        print("%s -- %d" % (k, v))
    return

def main():

    print ("Welcome to StuffMaster, v.0.47")
    print("Enter a command to add, view or quit.  Enter A, V, or Q: ")

    inventory = {} # empty dictionary

    while True: # get command, process command; quit when selected below
        pass

        # Get the command,
        command = getCommand().upper()
        # Call the appropriate function based on command
        if command == "A":
            invname = input("Enter item name to add: ")
            qty = int(input("Enter quantity: "))
            dict = {invname: qty}
            inventory = addToInventory(dict, inventory)
        elif command == "V":
            print("item -- count")
            print(viewInventory(inventory))
        elif command == "Q":
            break
        else:
            print("Not valid command, enter either A, V or Q.")
        # If unknown command, complain and prompt for reentry

    # here, we're quitting

    print ("Quitting. Final version of inventory is:")

    # print out final version of inventory
    viewInventory(inventory)

    print ("Exiting...")

main()
