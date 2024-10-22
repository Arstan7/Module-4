# Function to display the menu options
def display_menu():
    print("Please choose your option from the list below:")
    print("1. Learn Python")
    print("2. Learn Java")
    print("3. Go swimming")
    print("4. Have dinner")
    print("5. Go to bed")
    print("6. Watch a movie")
    print("7. Read a book")
    print("0. Exit")  # Option 0 to exit the program

# Function to handle the user's choice
def handle_choice(choice):
    if choice == 1:
        print("You chose to Learn Python")
    elif choice == 2:
        print("You chose to Learn Java")
    elif choice == 3:
        print("You chose to Go swimming")
    elif choice == 4:
        print("You chose to Have dinner")
    elif choice == 5:
        print("You chose to Go to bed")
    elif choice == 6:
        print("You chose to Watch a movie")
    elif choice == 7:
        print("You chose to Read a book")
    elif choice == 0:
        print("Exiting the program. Goodbye!")  # Exit message when user selects 0
    else:
        print("Invalid choice. Please try again.")  # For invalid inputs

# Main function to keep the program running in a loop
def main():
    choice = -1  # Initialize choice to a non-zero value to enter the loop
    while choice != 0:  # Continue looping until user selects option 0
        display_menu()  # Show the menu
        try:
            choice = int(input("Enter your choice: "))  # Get user input and convert to an integer
            handle_choice(choice)  # Process the choice using handle_choice function
        except ValueError:  # Handle case where input is not a valid number
            print("Please enter a valid number.")

# Entry point for the program
if __name__ == "__main__":
    main()
