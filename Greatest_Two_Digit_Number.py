def solution(S):
    Input = str(S)
    digit = 0
    placeholder = 0
    for c in range (1,len(Input)):
        Trial = int(Input[placeholder]+Input[placeholder+1])
        if Trial > digit:
            digit = Trial
        placeholder+=1
    return digit
