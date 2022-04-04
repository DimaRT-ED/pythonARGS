# This is a sample Python script.
# Created by Dag
# 4.4.22

import sys



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # total arguments
    n = len(sys.argv)
    print("Total arguments passed:", n)

    # Arguments passed
    print("\nName of Python script:", sys.argv[0])

    print("\nArguments passed:", end=" ")
    for i in range(1, n):
        print(sys.argv[i], end=" ")

