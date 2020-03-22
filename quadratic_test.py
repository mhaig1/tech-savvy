from quadratic_equation import quadratic



sol_1, sol_2 = quadratic(1, 2, 3)

if sol_1:  # same as if sol_1 is not None:
    print(f"The roots of the equation are {sol_1} and {sol_2}.")
else:
    print("No real number solutions.")