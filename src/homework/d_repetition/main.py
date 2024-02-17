# main.py content

#from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers
from repetition import get_factorial, sum_odd_numbers

def main():
    while True:
        print("""
        Homework 3 Menu
        1 - Factorial
        2 - Sum odd numbers
        3 - Exit
        """)
        choice = int(input("Choose an option: "))
        
        if choice == 1:
            num = int(input("Enter a number (0 < num < 10): "))
            while num <= 0 or num >= 10:
                num = int(input("Invalid. Enter a number (0 < num < 10): "))
            print("Factorial:", get_factorial(num))
        
        elif choice == 2:
            num = int(input("Enter a number (0 < num < 100): "))
            while num <= 0 or num >= 100:
                num = int(input("Invalid. Enter a number (0 < num < 100): "))
            print("Sum of odd numbers:", sum_odd_numbers(num))
        
        elif choice == 3:
            if input("Do you want to exit? (yes/no): ").lower() == 'yes':
                break
        
        if input("Do you want to continue? (yes/no): ").lower() == 'no':
            break

if __name__ == '__main__':
    main()
