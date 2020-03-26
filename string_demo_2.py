# built-in functions that take string(s) as parameter(s)

# print('John')
# input('Please enter your name:   ')
# type('John')
# len('John') 
# int('1') / float('1.23') / bool('john')

team = 'New England Patriots'
letter = team[1]
# print(letter)

# print(team[0])

# print(team[1.0])

print(len(team))

# last = team[len(team) - 1]
# a better way 
last = team[-1]
# print(last)

# for whatever in team:
#     print(whatever)


prefixes = 'JKLMNOPQ'
suffix = 'ack'

# for letter in prefixes:
#     print(letter + suffix)

# Exercise 1
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)


# string slicing

team = 'New England Patriots'

print(team[:11])
print(team[12:])


print(team[:])

print(team[::2])

print(team[::-1])


team = 'New England Patriots'
# team[12:20] = 'Seahawks'

new_team = team[:12] + 'Seahawks'
print(new_team)

print(team)

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'E'))


team = 'New England Patriots'
count = 0

for letter in team:
    if letter == 'a':
        count += 1

print(count)



# string methods

new_team = team.upper() 
print(new_team)

another_team = team.lower()
print(another_team)

print(team.split())

s = '    abcd     '
print(s.strip())

