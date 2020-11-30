marks=int(input("enter your marks"))

if marks<80:
    if marks<75:
        print("below average")
    elif marks<80:
        print("above average")
elif marks<90:
    print("distinction")
elif marks<=100:
    print("elite")
