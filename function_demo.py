# defining a function
def print_twice(whatever):
    print(whatever)
    print(whatever)


# calling a function
# print_twice('Lily answered the questions.') 



def double(a):
    return 2 * a
    print('The result is ', 2 * a) # this line will never be reached

# result = double(10)
# print(f'The result of the function with argument 10 is {result}.') 



# import myabs
from myabs import my_abs

b = -42
# abs_b = myabs.my_abs(b)
abs_b = my_abs(b)
print(abs_b)

# BE BACK at 12:41 