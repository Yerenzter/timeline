t1 = int(input("Enter the no. of seconds in 1st contestant: "))
t2 = int(input("Enter the no. of seconds in 2nd contestant: "))
t3 = int(input("Enter the no. of seconds in 3rd contestant: "))

time  = t1+t2+t3

if time < 60:
    if time < 10:
        print(f"00:0{time}")
    else:
        print(f"00:{time}")
else:
    if time >= 60:
        minute = time // 60
        second = time % 60
        if minute < 10 and second < 10:
            print(f"0{minute}:0{second}")
        elif minute >= 10 and second < 10:
            print(f"{minute}:0{second}")
        elif minute >= 10 and second >= 10:
            print(f"{minute}:{second}")
        else:
            print(f"0{minute}:{second}")
