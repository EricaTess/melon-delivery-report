def delivery_list(day, file):

    print(f"Day {day}")
    the_file = open(f"{file}")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    the_file.close()

delivery_list(1, "um-deliveries-20140519.txt")
