# file = open("file_ope/data.txt")
# data = file.read()
# file.close()
# print(data)

with open("file_ope/data.txt", "w") as file:
    file.write("good morning!")

with open("file_ope/data.txt") as file:
    print(file.read())