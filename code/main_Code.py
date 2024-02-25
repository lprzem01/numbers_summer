import numpy as np

def numbers_sum():
    user_input = input("Do you want to use a dataset different to defoult? (yes/no)")
    if user_input == "yes":
        data_file = input("Please provide directory for your data file")
    elif user_input == "no":
        data_file = "data/numbers.txt"
    else:
        print("ups I did't catch that.Try again and remeber to only input yes/no")
        user_input = input("Do you want to use a dataset different to defoult? (yes/no)")
    with open(data_file) as f:
        dataset = np.genfromtxt(f, delimiter=",")
    result = np.sum(dataset)
    return str(result)


with open(r"results/example_results", "w") as f:
    f.write(numbers_sum())