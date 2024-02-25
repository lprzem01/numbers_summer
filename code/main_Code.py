import numpy as np

def numbers_sum():
    """funtion that takes in a txt file of numbers separated by a comma and returns the sum of them in a results file. A defult file is provided if the user chooses not to provide one. """
    #determine if the defoult file is used
    user_input = input("Do you want to use a dataset different to defoult? (yes/no)")
    #make user input not case sensitive
    user_input = user_input.lower()
    #check if correct input was gived    
    while user_input !="yes" and user_input !="no":
        #if the correct input is not provided keep asking user to provide correct input with a prompt to clarify the correct input
        user_input = input("Ups I did not catch that, make sure you only type in yes or no ")
    #if initial input is yes ask user to provide their own datafile
    if user_input == "yes":
        data_file = input("Please provide directory for your data file ")
    # if the user input is no the defoult data file is set
    if user_input == "no":
        data_file = "data/numbers.txt" 
    #open the datafile (either user defined or defoult)
    with open(data_file) as f: 
        #read the file into a dataset with the delimiter set to a comma 
        dataset = np.genfromtxt(f, delimiter=",") 
    #set the result to be the sum of the numbers in the dataset
    result = np.sum(dataset)
    #store the results in a file in the results folder
    with open(r"results/example_results", "w") as f:
        f.write(str(result))
    return str(result)
