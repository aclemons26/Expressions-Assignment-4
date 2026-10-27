# Assignment Statement Forms Activity

# -----------------------------------------------------------------------------
# Scenario 1: Basic form
# Context: Setting up a user's display name from a registration form
# -----------------------------------------------------------------------------
display_name = "Jordan Lee"                    # basic assignment
greeting = "Welcome, " + display_name           
print(greeting)


# -----------------------------------------------------------------------------
# Scenario 2: Tuple assignment 
# Context: Unpacking first and last name from a database record
# -----------------------------------------------------------------------------
first_name, last_name = "Jordan", "Lee"         # tuple assignment
full_name = first_name + " " + last_name        
print("Full name:", full_name)


# -----------------------------------------------------------------------------
# Scenario 3: Sequence assignment (generalized)
# Context: Extracting individual characters from a product SKU code
# -----------------------------------------------------------------------------
sku = "ABCD"
letter1, letter2, letter3, letter4 = sku        # sequence assignment
checksum = ord(letter1) + ord(letter4)          
print("SKU letters:", letter1, letter2, letter3, letter4)
print("Simple checksum:", checksum)


# -----------------------------------------------------------------------------
# Scenario 4: Extended sequence unpacking (Python 3.x)
# Context: Eeading list into the latest value and history
# -----------------------------------------------------------------------------
readings = [72.1, 71.8, 73.4, 70.9, 72.5]
latest, *history = readings                     # extended 
average_history = sum(history) / len(history)   
print("Latest reading:", latest)
print("History average:", round(average_history, 2))

#----------------------------------------
#Scenerio 5:  Using an Expression
# Context: Calculate the total cost of buying 3 books
notebook_price = 2.50
quantity = 3
total_cost = notebook_price * quantity
print("The total cost of the notebooks is $", total_cost)
