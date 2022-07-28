'''Given a list of numbers, write a code that
returns the sum of the second maximum and the
second minimum value in te list.'''

def solution(list):
    list.sort()
    return list[1]+list[len(list)-2]
