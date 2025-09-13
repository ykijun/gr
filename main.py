# f = open("example.txt","r")
# lines = []
# for line in f:
#     lines.append(line.strip())
# f.close()
# print(lines)

# with open("example.txt","r") as f:
#     lines = f.readlines()
# print(lines)

# with open("example.txt","w") as f:
#     f.write("\nkiwi")

# with open ("example.txt", "r+") as f: 
#     numbers = f.read()
#     numbers = numbers.split()
#     numbers = [int(i) for i in numbers]
#     SUM = sum(numbers) 
#     f.write("\n" + str(SUM))

# l = [1, 2, 3, 4, 5]
# list_to_str = [str(i) for i in l]
# s = " ".join(list_to_str) 
# with open ("example.txt", "w") as f: 
#     f.write(s)




with open("example.txt", "w") as f: 
    for i in range (3): 
        number = input() 
        f.write(number + "\n")