import random

def find_num(count, random_number):
    number = int(input())
    if number == random_number:
        print("Congratulations! you guessed the number correctly in {} tries.".format(count))
    elif number < random_number:
        print('Number is more than {}'.format(number))
        count += 1
        find_num(count, random_number)
    else:
        print('Number is less than {}'.format(number))
        count += 1
        find_num(count, random_number)
    pass


print("Enter the Minimum number :")
minimum_number = int(input())

print("Enter the Maximum number :")
maximum_number = int(input())

count = 1
random_number = random.randint(minimum_number, maximum_number)

print('Enter a number to guess :')
find_num(count, random_number)