counts = {}
# hi = "hello"
# counts["hi"] =1
# # counts["hello"] = counts["hello"] +1

# print(counts)


with open("tutoralhell\\story2.txt", "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            
            if word in counts:
                counts[word] += 1
            else: 
                counts[word] = 1

for word, count in counts.items():
    print(f"{word}: {count}")
            
    
 