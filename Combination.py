
"""
Created on Tue Feb  5 14:52:27 2019

@author: sagar
"""
import array
import re

def DivideConquer(input_sequence, combination_size):
    length_of_input = len(input_sequence)
    temp_sequence = [0]*combination_size
    combination(input_sequence,temp_sequence,0,length_of_input-1,0,combination_size)

def combination(input_sequence, temp_sequence, start, end, index, combination_size):

    if (index == combination_size):
        for j in range(combination_size):
            print(temp_sequence[j])
        print()
        return
    else:
        i = start
        while(i <= end and end - i + 1 >= combination_size - index):
            temp_sequence[index] = input_sequence[i]
            combination(input_sequence, temp_sequence, i + 1, end, index + 1, combination_size)
            i+=1

input_sequence = re.split(r'[;,\s]\s*', input("enter a list"))
combination_size = int(input("enter the size of combination"))
DivideConquer(input_sequence, combination_size)