with open("story.txt", "r") as file:
    total =0
    for line in file:
       word = line.split()
       print(word)
       count = len(word)
       total += count


    print(total)

        