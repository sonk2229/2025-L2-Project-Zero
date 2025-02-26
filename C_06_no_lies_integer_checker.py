# Functions go here
def int_check(question):
        """Checks users enter an integer"""

        error = "Oops - Please enter an number more than zero."

        while True:

            try:
                # Return the response if it's an integer
                response = int(input(question))

                return response

            except ValueError:
                print(error)


# Main Routine goes here

# loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = input("Name: ")  # replace with call to 'not blank' function!

    # ask for their age check it.s between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue
    else:
        print(f"{name} bought a ticket")
