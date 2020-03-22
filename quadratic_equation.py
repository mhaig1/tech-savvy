import math


def quadratic(a, b, c):
    """
    returns the two solutions of a quadratic function, a*x**2+b*x+c = 0, if there are real number solutions

    a, b, c: float numbers
    """
    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        x_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x_1, x_2
    else:
        # print('No real number solutions.')
        return None, None


# TODO: Done! what to return when there is no real number solutions
# TODO: Done! wrap test code into main function


def main():
    a = float(input("Please enter a number: "))
    b = float(input("Please enter a number: "))
    c = float(input("Please enter a number: "))

    sol_1, sol_2 = quadratic(a, b, c)

    if sol_1:  # same as if sol_1 is not None:
        print(f"The roots of the equation are {sol_1} and {sol_2}.")
    else:
        print("No real number solutions.")


if __name__ == "__main__":
    main()

