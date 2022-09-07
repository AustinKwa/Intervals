#  File: Intervals.py

#  Description: Collapse all overlapping intervals and prints them in ascending order
#               from lowest to highest values

#  Student Name: Austin Kwa

#  Student UT EID: ak38754

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E 

#  Unique Number: 51125

#  Date Created: 1/29/2022

#  Date Last Modified: 1/31/2022

import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def sort_tuples_list (tuples_list):
    # sorted the list of tuples
    sorted_list = []
    while len(tuples_list) > 0:
        min_value = tuples_list[0][0]
        min_tuple = tuples_list[0]
        for i in range(len(tuples_list)):
            if min_value > tuples_list[i][0]:
                min_value = tuples_list[i][0]
                min_tuple = tuples_list[i]
        sorted_list.append(min_tuple)
        tuples_list.remove(min_tuple)
    
    return sorted_list

def merge_tuples (tuples_list):
    # compares tuples side by side and merges them
    tuples_list = sort_tuples_list(tuples_list)
    i = 0
    while i < len(tuples_list) - 1:
        restart = False
        if tuples_list[i][1] >= tuples_list[i + 1][0]:
            if tuples_list[i][1] >= tuples_list[i + 1][1]:
                tuples_list.remove(tuples_list[i + 1])
                tuples_list = sort_tuples_list(tuples_list)
                restart = True
            else:
                tuple1 = tuples_list[i]
                tuple2 = tuples_list[i + 1]
                tuples_list.remove(tuple1)
                tuples_list.remove(tuple2)
                tuples_list.append((tuple1[0], tuple2[1]))
                tuples_list = sort_tuples_list(tuples_list)
                restart = True
        if restart == True:
            i = 0
        else:
            i += 1

    return tuples_list


# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    sorted_list = []
    while len(tuples_list) > 0:
        min_size = tuples_list[0]
        for i in range(len(tuples_list)):
            if (min_size[1] - min_size[0]) > (tuples_list[i][1] - tuples_list[i][0]):
                min_size = tuples_list[i]
        sorted_list.append(min_size)
        tuples_list.remove(min_size)

    return sorted_list        



# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
    assert merge_tuples([(1,2)]) == [(1,2)]
    # write your own test cases

    assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
    # write your own test cases

    return "all test cases passed"

def main():
    # open file intervals.in and read the data and create a list of tuples
    num_tuples = sys.stdin.readline()
    num_tuples = num_tuples.split()
    num_tuples = int(num_tuples[0])

    temp_list = []
    tuple_list = []
    for i in range(num_tuples):
        temp_list.append(sys.stdin.readline())
        temp_list[i] = temp_list[i].split()
        tuple_list.append((int(temp_list[i][0]), int(temp_list[i][1])))

    merged = merge_tuples(tuple_list)
    print(merged)

    sorted = sort_by_interval_size(merged)
    print(sorted)

    #print (test_cases())

    # write the output list of tuples from the two functions

if __name__ == "__main__":
  main()