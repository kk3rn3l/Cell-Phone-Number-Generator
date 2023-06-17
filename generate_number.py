#!/bin/python

numbers = []

for i in range(10):
    if i not in [6, 7, 8, 9]: #replace any digit or comment out this section if you want 6,7,8,9 in the place of {i} 
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for o in range(10):
                                number = f'+923{i}{j}{k}{l}{m}{n}{o}23'  #Change +923 with country code and if you want to add last digits you can do that or remove 23
                                numbers.append(number)

# Save the generated numbers in a text file
with open('output.txt', 'w') as file:
    for number in numbers:
        file.write(number + '\n')
