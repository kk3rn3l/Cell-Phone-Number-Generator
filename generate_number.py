#!/usr/bin/python

numbers = []

for i in range(10):
    # Uncomment the following line if you want to exclude 0, 1, 2, 3, 4, 6, 7, 8, 9
    # if i not in [0, 1, 2, 3, 4, 5]:  # This will exclude 6, 7, 8, 9 if desired
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    for n in range(10):
                        for o in range(10):
                            for p in range(10):
                                for q in range(10):
                                    number = f'+923{i}{j}{k}{l}{m}{n}{o}{p}{q}'  # Change +923 to the desired country code
                                    numbers.append(number)

# Save the generated numbers in a text file
with open('output.txt', 'w') as file:
    for number in numbers:
        file.write(number + '\n')
