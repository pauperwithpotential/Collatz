'''
Write function name collatz() with one parameter, number
If number is even, print and return number // 2
If number is odd, print and return 3 * number + 1
'''

def collatz(number):
        newNumber = 0
        if number % 2 == 0:
            newNumber = number // 2
            
        elif number % 2 == 1:
            newNumber = 3 * number + 1

        print(newNumber)
    
        if newNumber > 1:
            collatz(newNumber)


while True:
    print('Enter a number:')
    number = input()
    try:
        print(collatz(int(number)))
    except ValueError:
        print('Must enter an integer')



    
