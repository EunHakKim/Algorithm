while True:
    try:
        words=input()
    except:
        break
    small=0
    big=0
    num=0
    blank=0
    for x in words:
        if x.islower():
            small+=1
        elif x.isupper():
            big+=1
        elif x.isdigit():
            num+=1
        elif x==' ':
            blank+=1

    print(small,big,num,blank)