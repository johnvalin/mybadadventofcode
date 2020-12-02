file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
#part 1
counter = 0
for line in Lines: 
    brokenLine = line.strip().split()
    # print(brokenLine)
    minMax = brokenLine[0].split('-')
    importantChar = brokenLine[1][0]
    password = brokenLine[2]
    if(password.count(importantChar) >= int(minMax[0]) and password.count(importantChar) <= int(minMax[1])):
        counter += 1
        # print("valid")
print(counter)


#part 2
counter = 0
for line in Lines: 
    brokenLine = line.strip().split()
    # print(brokenLine)
    positions = brokenLine[0].split('-')
    importantChar = brokenLine[1][0]
    password = brokenLine[2]
    if((password[int(positions[0])-1] == importantChar) ^ (password[int(positions[1])-1]== importantChar)):
        counter += 1
        # print("valid")
print(counter)