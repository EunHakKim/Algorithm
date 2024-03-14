word=input()

sum=0

for x in word:
    if "A"<=x<="C":
        sum+=3
    elif "D"<=x<="F":
        sum+=4
    elif "G"<=x<="I":
        sum+=5
    elif "J"<=x<="L":
        sum+=6
    elif "M"<=x<="O":
        sum+=7
    elif "P"<=x<="S":
        sum+=8
    elif "T"<=x<="V":
        sum+=9
    elif "W"<=x<="Z":
        sum+=10   

print(sum)                   