#get the rows
#programme of printing patterns of numbers
rows = int(input("enter the number of rows"))
for i in range(rows):
    for j in range (i + 1):
        print(j + 1,end=" ")
    print("\n")