import itertools


for iteration, permuation in enumerate(itertools.permutations("0123456789")):
    if iteration == 999_999:
        print("".join(permuation))
