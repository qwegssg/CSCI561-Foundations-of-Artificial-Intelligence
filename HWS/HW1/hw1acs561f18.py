with open("input.txt") as input_file:
    lines = input_file.read().splitlines()
    with open("output.txt", "w") as output_file:
        for line in lines:
            data = line.split(",")
            if data[1] == "Dirty":
                output_file.write("Suck\n")
            elif data[0] == "A":
                output_file.write("Right\n")
            elif data[0] == "B":
                output_file.write("Left\n")