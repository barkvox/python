
# Complete the countingValleys function below.
def countingValleys(n, s):
    i = 0
    level = valley = 0
    while i<n:
        if s[i] == 'U':
            level+=1
            if level == 0:
                valley+=1
        else:
            level-=1
        i+=1  
    return valley

print(countingValleys(8, 'UDDDUDUU'))
