def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    # Input validation loop
    while True:
        num = input("Enter a non-negative integer to calculate its factorial: ")
        
        # Check if the input is a valid non-negative integer
        if num.isdigit():
            num = int(num)
            break
        else:
            print("Invalid input! Please enter a non-negative integer.")

    # Calculate and display the factorial
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers.")
    else:
        print(f"The factorial of {num} is {factorial(num)}")

if __name__ == "__main__":
    main()