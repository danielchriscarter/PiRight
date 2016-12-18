import csv
import random

def randomise(list):
    randomList = []
    while(len(list)>0):
        randomList.append(list.pop(random.randrange(0,len(list))))
    return randomList

questions = []
with open('questions.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        questions.append(row)

questions = randomise(questions)

for q in questions:
    print(q[0])
    print("A: " + q[1])
    print("B: " + q[2])
    print("C: " + q[3])
    print("D: " + q[4])
    if(input("What is your answer...").upper()==q[5]):
        print("Well done!")
    else:
        print("Unfortunately that is not correct")
    print()
