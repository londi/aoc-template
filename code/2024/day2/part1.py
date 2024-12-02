import os
import re

def main(test_input=False):
    sum = 0
    fileName = 'test_input.txt' if test_input else 'input.txt'
    with open(os.path.dirname(os.path.realpath(__file__)) + '/' + fileName, 'r') as input_file:
        
        for line in input_file:
            elements = line.replace("\n", "").split(" ")
            # lastElement = int(elements.pop(0))
            # factor = 0
            # safe = True
            # while len(elements) > 0:
            #     elem = int(elements.pop(0))
            #     diff = lastElement - elem
                
            #     if diff == 0:
            #         # print("not safe. elem equal lastElement")
            #         safe = False
            #         break
                
            #     diffFactor = f(diff)
            #     if (factor != 0 and diffFactor != factor):
            #         # print("not safe. diffFactor not same")
            #         safe = False
            #         break
            #     factor = diffFactor
            #     if abs(diff) > 3:
            #         # print("not safe. diff to high")
            #         safe = False
            #         break
                
            #     lastElement = elem
                
            # if safe:
            #     print("safe")
            #     sum = sum + 1
            # else:
            #     print("not safe")
                
            if is_safe(elements):
                print("safe")
                sum = sum + 1
            else:
                print("not safe")


        
    return sum

def f(diff):
    return -1 if diff > 0 else 1


def is_safe(elements):
    lastElement = int(elements.pop(0))
    factor = 0
    safe = True
    while len(elements) > 0:
        elem = int(elements.pop(0))
        diff = lastElement - elem
        
        if diff == 0:
            # print("not safe. elem equal lastElement")
            safe = False
            break
        
        diffFactor = f(diff)
        if (factor != 0 and diffFactor != factor):
            # print("not safe. diffFactor not same")
            safe = False
            break
        
        factor = diffFactor
        if abs(diff) > 3:
            # print("not safe. diff to high")
            safe = False
            break
        lastElement = elem
        
    return safe

if __name__ == '__main__':
    print(main(False))
    # 635 too high
    # 246 too low
    # 624 is right