### This is python code for  finding the average value of numbers entered in the prompt and separated by spaces
## The following are the steps to achieve this:
# Step1. defining the function - the function does not have any parameters therefore , it will not accept any arguement
````
def average_number():
````

# Step2. taking input from the prompt and saving it to the a variable
````
numbers = input("Enter a list of numbers , separated by space: ")
````

# Step3. using the split method to split the input string into a list of substring and storin the result into a variable
````
list_of_numbers = numbers.split()
````
# Step4. Converting the numbers entered into integers, using the list comprehension syntax
````
list_of_integers = [int(integer)for integer in list_of_numbers]
````
# Step5. Using a for loop , add the numbers in the list to the variable sum . Check if the number of terms is equal to zero to avoid the error of division by zero 

# Step 4 . Define the sum variable and initialize it with the value zero, find the number of terms using the len method 

````
number_of_terms = len(list_of_integers)
    for number in list_of_integers:
        sum += number
    if number_of_terms != 0:
        average = sum/number_of_terms
        print ("The Average is", average)
    else:
        print("Cannot calculate average. Please provide at least one number.")

````

for any questions , call me @ +254 714296170




