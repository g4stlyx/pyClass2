import random
random.seed()

sum = 0
i = 0
numbers= []

for i in range(0, len(numbers),1):
        numbers[i] = int(random.random()*11)
        if numbers[i] %2 == 0:
                sum= sum + numbers[i]
        

print(sum)



input("press enter to exit")
