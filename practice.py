def average_number():
    numbers = input("Enter a list of numbers , separated by space: ")
    list_of_numbers = numbers.split()
    list_of_integers = [int(integer)for integer in list_of_numbers]
    sum = 0
    number_of_terms = len(list_of_integers)
    for number in list_of_integers:
        sum += number
    if number_of_terms != 0:
        average = sum/number_of_terms
        print ("The Average is", average)
    else:
        print("Cannot calculate average. Please provide at least one number.")

average_number()
