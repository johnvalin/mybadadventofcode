file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
allInputs = []
# Strips the newline character 
for line in Lines: 
    allInputs.append(int(line.strip()))

#print(allInputs)
counter = 0

#part1
for num1 in allInputs:
    for num2 in allInputs:
            if(num1!=num2 and num1+num2==2020 and counter==0):
                print(str(num1*num2))
                counter+=1

counter = 0
#part2
for num1 in allInputs:
    for num2 in allInputs:
        for num3 in allInputs:
            if(num1!=num2 and num2!=num3 and num1!=num3 and num1+num2+num3==2020 and counter==0):
                print(str(num1*num2*num3))
                counter+=1