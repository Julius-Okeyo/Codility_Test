'''Write a code to print characters from a string
that are present at an even index number.
For example given the input string "python"
the output characters will be p,t,o'''

def solution(string):
    input = str(string)
    output = ''
    for i in range(len(input)):
        if i % 2 == 0:
            output += input[i] + ','
    return output
