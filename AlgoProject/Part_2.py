import itertools

# define the digits that are still functional
usable_digits = [1, 3, 5, 7, 8, 9]

# generate all possible 3-digit combinations without repetition
possible_combinations = list(itertools.permutations(usable_digits, 3))

# print out all possible combinations
print("Total combinations:", len(possible_combinations))
print("Possible combinations:", possible_combinations)

# assume Algo Jones opens the lock with the 20th combination
successful_combination = possible_combinations[19]  # index 19 for the 20th element
print("Successful combination on 20th try:", successful_combination)
