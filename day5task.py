# marks=int(input("enter your marks"))

# if marks<80:
#     if marks<75:
#         print("below average")
#     elif marks<80:
#         print("above average")
# elif marks<90:
#     print("distinction")
# elif marks<=100:
#     print("elite")


marks = int(input('Enter the marks: '))

if 70 <= marks < 80:
	    print('checking 70-75 category and 75-80 category....... ')
	    if 70 <= marks <= 75:
	        print('Average')
	    else:
	        print('above average')
elif 80 <= marks <90:
	    print('Distinction')
elif 90 <= marks <=100:
	    print('elite')
elif 0 <= marks < 70:
	    print('Poor students')
else:
		print('Give valid marks within 100')
