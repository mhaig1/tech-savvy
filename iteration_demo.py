result = 0 

for i in range(1000):
    print(f'In interation {i}, current result is {result}.')
    
    result += i+1

    print(f'After adding {i+1}, the result becomes {result}.')
    print()

print(f'Final result is {result}.')

