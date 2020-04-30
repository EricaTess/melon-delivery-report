def delivery_list(day, file):
    """Given a number and a text file of deliveries.

    Will generate a list of the quantity of items delivered
    and total cost."""

    #Uses the day parameter to display which day
    print(f"Day {day}")

    #Assigns the txt file to the_file
    the_file = open(f"{file}")

    #iterates through each line in the file
    for line in the_file:

        #removes the whitespace
        line = line.rstrip()

        #each element between '|' is split into a list
        words = line.split('|')

        #the first, second, and third word of the list is defined
        melon = words[0]
        count = words[1]
        amount = words[2]

        #message is printed for each line
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    #file is closed    
    the_file.close()


#call function with day and file
delivery_list(1, "um-deliveries-20140519.txt")
delivery_list(2, "um-deliveries-20140520.txt")
delivery_list(3, "um-deliveries-20140521.txt")

