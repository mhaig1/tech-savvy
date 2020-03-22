# age = int(input('Please enter your age: '))

# if age >= 6:
#     print('teenager')
#     print('your age is ', age)


# elif age >= 18:
#     print('adult')
# else:
#     print('kid')

def countdown(n):
    import time
    time.sleep(1)

    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

countdown(5) 