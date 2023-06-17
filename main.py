numbers = []

for i in range(10):
    #if i not in [6, 7, 8, 9]:
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    for m in range(10):
                        for n in range(10):
                            for o in range(10):
                                number = f'03{i}{j}{k}{l}{m}{n}{o}' #Change 03 with country code
                                numbers.append(number)

# Save the generated numbers in a text file
with open('output.txt', 'w') as file:
    for number in numbers:
        file.write(number + '\n')
