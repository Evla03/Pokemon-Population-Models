import random
import math
import csv


MalePop = 14
FemalePop = 2
tick = 0
eggs = [0 for i in range(21)]

with open('BulbasaurPopulationNoHuman.csv', 'a', newline='') as csv_file:
        fieldnames = ['tick', 'females', 'males']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        csv_file.close()

while True:
    with open('BulbasaurPopulationNoHuman.csv', 'a', newline='') as csv_file:
        fieldnames = ['tick', 'females', 'males']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'tick': tick, 'females': FemalePop, 'males': MalePop})
        csv_file.close()
    tick += 1
    print("Tick:", tick)
    for x in range(FemalePop):
        death = random.randint(1,10000)
        if death <= 243:
            FemalePop += -1
            

    for x in range(MalePop):
        death = random.randint(1,10000)
        if death <= 243:
            MalePop += -1
            
    
    if eggs[0] > 0:
        print (eggs[0], "Bulbasaur eggs are hatching!")
        for x in range(eggs[0]):
            sexroll = random.randint(1,8)
            if sexroll <= 7:
                MalePop += 1
            else:
                FemalePop += 1
    
    eggs[0:9] = [eggs[i] + eggs[i+1] for i in range(9)]
    eggs[10:19] = [eggs[i] - eggs[i+1] + eggs[i+2] for i in range(10, 19)]



    if MalePop >=1:
        for x in range(FemalePop):
            egg = random.randint(1,100)
            if egg <= 50:
                eggs[20] += 1
                
    elif FemalePop >=1:
        
        for x in range(FemalePop):
            egg = random.randint(1,100)
            if egg <=10:
                eggs[20] += 1

              
    
    print("Total Population:", FemalePop+MalePop)
    print("Females:", FemalePop)
    print("Males:", MalePop)
    print("")


    if FemalePop+MalePop >= 20000:
        print("Population max reached")

        break
    elif not any(eggs) or not FemalePop:
        print("Extinction")
        break
