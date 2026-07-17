import sys
import time


def validate_user_input():
    while True:
        user_number = input("Enter a starting number (greater than 0) or QUIT:\n> ")
        if user_number.lower() == "quit":
            sys.exit()
        if not user_number.isdecimal():
            continue

        user_number = int(user_number)
        if user_number>0:
            return user_number

def main():
    print("""
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:    
1. If n is even, the next number n is n / 2.
2. If n is odd, the next number n is n * 3 + 1.
3. If n is 1, stop. Otherwise, repeat.
    """)

    number = validate_user_input()
    print(number, end='', flush=True)
    while number != 1:
        if number%2==0:
            number = number /2
            number = int(number)
        elif number%2==1:
            number = number*3+1
            number = int(number)
        print(', ' + str(number), end='', flush=True)
        time.sleep(0.1)

if __name__=='__main__':
    main()
