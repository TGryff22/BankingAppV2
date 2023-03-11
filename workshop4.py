# Declare a class and give it the name User
# Give the User class three instance attributes: name, pin, and password

class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        return name

    def change_pin(self, pin):
        self.pin = pin
        return pin

    def change_password(self, password):
        self.password = password
        return password


''' Driver Code for Task 1
# instantiate an object from the User class, providing the name, pin, and password as arguments
user1 = User("Bob", 1234, "password")
# print statement to print the name, pin, and password attributes of this object
print(user1.name, user1.pin, user1.password)
'''

''' Driver Code for Task 2 
user1 = User("Bob", 1234, "password")
print(user1.name, user1.pin, user1.password)
# Call each of the three methods you created to change the name, pin, and password
print(user1.change_name("Bobby"), user1.change_pin(
    4321), user1.change_password("newpassword"))
'''

# Declare a class and give it the name BankUser.
# Have the BankUser class inherit the User class.


class BankUser(User):
    # It should inherit the instance attributes of name, pin, and password.
    def __init__(self, name, pin, password):
        # Use the super() function to initialize these inherited attributes using the superclass
        super().__init__(name, pin, password)
        self.balance = 0  # Give the BankUser class its own instance attribute

    # Write three methods for the BankUser class:
    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount

    def deposit(self, deposit_amount):
        self.balance += deposit_amount

    # Create two more methods for the BankUser class:
    def transfer_money(self, user, amount):
        # Transfers money to another User if
        print("You are transferring $" + str(amount), "to", user.name)
        print("Authentication required")
        # correct PIN is given for the transferring User. Also return a Boolean value of True.
        pincode = int(input("Enter your PIN: "))
        # If an incorrect PIN is given, return a Boolean value of False.
        if pincode != self.pin:
            print("Invalid PIN. Transaction canceled.")
            return False
        print("Transfer authorized")
        print("Transferring $" + str(amount) + " to " + user.name)
        self.balance -= amount
        user.balance += amount

        return True

    def request_money(self, user, amount):
        print("You are requesting $" +
              str(amount), "from", user.name)
        print("User authentication is required...")

        # Will ask for the PIN of the User receiving the request for money.
        pin = int(input("Enter " + user.name + "'s PIN: "))
        if pin != user.pin:
            print("Invalid PIN. Transaction canceled.")
            return False   # If either is incorrect, return False.
        # If credentials are correct
        # Will ask for and validate the password of the User requesting money as well
        password = input("Enter your password: ")
        if password != self.password:
            print("Invalid password. Transaction canceled.")
            return False   # If either is incorrect, return False.

        print("Request authorized")
        print(user.name + " sent $" + str(amount))
        # Then complete the transfer, removing money from one account and adding the same amount to the other.
        user.balance -= amount
        self.balance += amount
        # If both the PIN or password requested are correct, return True.
        return True


''' Driver Code for Task 3 
user1 = BankUser("Bob", 1234, "password")  # Instantiate an object of the BankUser class, providing arguments for the name, pin, and password
print(user1.name, user1.pin, user1.password, user1.balance)  # Print the attributes of the BankUser object
'''

''' Driver Code for task 4 
# Instantiate an object of the BankUser class, providing arguments for the name, pin, and password.
user1 = BankUser(
    "Bob", 1234, "password")  # Instantiate an object of the BankUser class 
user1.show_balance()   # Call the show_balance() method of the object.
user1.deposit(1000.0)   # Call the deposit() method, depositing some positive number.
user1.show_balance()   # Call the show_balance() method once again.
user1.withdraw(500.0)   # Call the withdraw() method, withdrawing some number lower than what was deposited.
user1.show_balance()   # Call the show_balance() method again.
'''

# Instantiate an object of the BankUser class, providing arguments for the name, pin, and password.
user1 = BankUser("Bob", 1234, "password")
# Instantiate a second object of the BankUser class, providing different arguments.
user2 = BankUser("Alice", 5678, "alicepassword")
# Deposit $5000 into the account of this second user using the deposit() method.
user2.deposit(5000)
user2.show_balance()   # Show the balance of the second user.
user1.show_balance()   # Show the balance of the first user.
print()

# Have the second user transfer $500 to the first user, using its transfer_money() method.
transferred = user2.transfer_money(user1, 500)
# Show the balance of each user.
user2.show_balance()
user1.show_balance()
print()
'''
If the money transfer is successful, have the second user request some money from the 
first user, using its request_money() method (this means that there should be an if 
statement in your test code checking for the success of the first transaction).
'''
if transferred:
    user2.request_money(user1, 250)
    # Show the balance of both users.
    user2.show_balance()
    user1.show_balance()


'''
Bonus Task 1
Add validation thus that only positive numbers can be deposited, withdrawn, transferred, and requested. If a string or negative number is entered, an appropriate message should be shown. 

Bonus Task 2
Take Task 1 further and update the transfer_money() and request_money() methods so that no amount greater than what is available can be transferred from one account to another.

Bonus Task 3
Decide on validation parameters for the name, password, and PIN and update the change_name(), change_pin(), and change_password() methods to enforce those parameters. 
Examples: 
    The username can only be changed if the new name is >= 2 characters and <= 10 characters.
    The password can only be changed if the new password is >= 5 characters.
    The PIN can only be changed if the new PIN is exactly 4 numbers. 
    The new value cannot be the same as the previous value.
    No space characters are allowed. 

Bonus Task 4
Format the outputs so that dollar amounts display 2 digits after the decimal point instead of 1. 
Example: $500.00 instead of $500.0.

Bonus Task 5
Add an instance attribute on the BankUser class called on_hold and initialize it to False. 
Add a method that can be called to toggle this on_hold class to the opposite of its current Boolean value. (So if it is True, flip it to False, and if it is False, flip it to True.)
Add a check for each of the withdraw(), deposit(), transfer_money(), and withdraw_money() methods thus that if the on_hold attribute for any user involved in the transaction is True, the transaction is rejected with an appropriate failure message.
'''
