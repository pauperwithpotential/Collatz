'''
Write function name collatz() with one parameter, number
If number is even, print and return number // 2
If number is odd, print and return 3 * number + 1
Let user type in an integer that keeps calling collatz() till it returns the value 1
Add try and except statements to detect whether user types in a non-integer string
'''

def collatz(number):
        if number % 2 == 0:
            number = number // 2
            
        elif number % 2 == 1:
            number = 3 * number + 1

        print(number)
    
        if number > 1:
            collatz(number)        

while True:
    try:
        print('Enter any number:')
        number = int(input())
        collatz(number)
    except ValueError:
        print('Must enter an integer')



    
