def factorial(n):
    """Recursive function to calculate the factorial of a number."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    try:
        # Ask the user for input
        num = int(input("Enter a non-negative integer to calculate its factorial: "))

        # Input validation
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers.")
        else:
            # Calculate and display the factorial
            print(f"The factorial of {num} is {factorial(num)}")

    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()

print("trst")
print("karthik")
