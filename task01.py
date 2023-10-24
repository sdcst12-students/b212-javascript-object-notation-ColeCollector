#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891


class task1:
    def __init__(self,file):
        import json
        lineData = json.loads(open(file,"r").read())
        biggestnum = 0

        for i in lineData:
            if int(i) > biggestnum:
                biggestnum = int(i)

        print(biggestnum)



task1("task01a.txt")
task1("task01b.txt")
task1("task01c.txt")