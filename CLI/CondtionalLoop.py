int1 = 77
int2 = 55
int3 = 23

# if conditional loop
if int1 > int2:
    print(int1, 'is grater than', int2)
'''
InPut: int1 = 44, int2 = 33
OutPut:
44 is grater than 33
'''


# if else conditional loop
if int1 > int2:
    print(int1, 'is grater than', int2)
else:
    print(int1, 'is less than', int2)
'''
InPut: int1 = 22, int2 = 33
OutPut: 22 is less than 33
'''


# nested if else conditional loop
if int1 > int2 > int3:
    print(int1, 'is grater')
elif int2 > int3 > int1:
    print(int2, 'is grater')
elif int3 > int1 > int2:
    print(int3, 'is grater')
elif int2 == int1 == int3:
    print('all are equal')
else:
    print('i m confuse..')
'''
InPut: int1 = 22, int2 = 33, int3 = 55
OutPut: i m confuse..
InPut: int1 = 88, int2 = 77, int3 = 55
OutPut: 88 is grater
InPut: int1 = 33, int2 = 55, int3 = 44
OutPut: 55 is grater
InPut: int1 = 44, int2 = 22, int3 = 77
OutPut: 77 is grater
InPut: int1 = 33, int2 = 33, int3 = 33
OutPut: all are equal
'''


# while loop
i = 7
while i < 10:
    print(i, 'you are less than 10')
    i += 1;
'''
OutPut:
7 you are less than 10
8 you are less than 10
9 you are less than 10
'''


# do while loop
''' in 'C'
int i = 1;
do{
  printf("%d\n", i);
  i = i + 1;
} while(i <= 3);
'''
i = 1
while True:
    print('in Do While loop: ', i)
    i += 1
    if i > 3:
        break
'''
OutPut:
in Do While loop:  1
in Do While loop:  2
in Do While loop:  3
'''