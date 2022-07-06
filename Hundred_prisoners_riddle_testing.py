#In this problem, 100 numbered prisoners must find their own numbers in one of 100 drawers in order to survive.
#The rules state that each prisoner may open only 50 drawers and cannot communicate with other prisoners.

#Surprisingly, there is a strategy that provides a survival probability of more than 30%. The key to success is that the prisoners do not have to decide beforehand which drawers to open.
#Each prisoner can use the information gained from the contents of every drawer he already opened to help decide which one to open next.
#Another important observation is that this way the success of one prisoner is not independent of the success of the other prisoners, because they all depend on the way the numbers are distributed.
#To describe the strategy, not only the prisoners, but also the drawers are numbered from 1 to 100, for example row by row starting with the top left drawer. The strategy is now as follows:
#[1]Each prisoner first opens the drawer with his own number.
#[2]If this drawer contains his number he is done and was successful.
#[3]Otherwise, the drawer contains the number of another prisoner and he next opens the drawer with this number.
#[4]The prisoner repeats steps 2 and 3 until he finds his own number or has opened 50 drawers.
#By starting with his own number, the prisoner guarantees he is on a sequence of boxes containing his number. The only question is whether this sequence is longer than 50 boxes.

#Program to simulate prisoners and check if they really have more than 30% chance of succeding

import random
list_of_prisoners = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,
                       38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,
                       70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
random.shuffle(list_of_prisoners)
print(list_of_prisoners)
loop_length = 1
total_cases = 0
passed_cases = 0
failed_cases = 0

def testforOnecase():
    for i in range(1, 101):
        loop_length = 1
        drawer_number = i

        while (loop_length < 100):
            if list_of_prisoners[drawer_number] == i:
                break
            else:
                drawer_number = list_of_prisoners[drawer_number]
                loop_length += 1
        if loop_length > 50:
            return 0
        # print(str(i)+" "+str(successful)+", loop len ="+str(loop_length))

while 1:
    random.shuffle(list_of_prisoners)
    if testforOnecase() == 0:
        failed_cases = failed_cases +1
        total_cases = total_cases +1
    else:
        passed_cases = passed_cases + 1
        total_cases = total_cases + 1
    if total_cases%100 == 0:
        print("passed: " + str(passed_cases))
        print("failed: " + str(failed_cases))
        print("total: " + str(total_cases))
        print("Chance of passing: " + str(passed_cases * 100 / total_cases) + "%")
        if total_cases%1000 == 0:
            print("press something")
            input()