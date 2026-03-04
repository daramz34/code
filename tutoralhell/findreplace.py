with open("input.txt", "r") as infile:
    with open("output.txt", "w") as outfile:
        for line in infile:
            new_line = line.replace("cat","dog")
            outfile.write(new_line)
