def c_to_f(c):
    """Convert from Celsius to Fahrenheit"""
    return c * (9.0/5.0) + 32


def f_to_c(f):
    """Convert from Fahrenheit to Celsius"""
    return (f - 32) * (5.0/9.0)


if __name__ == "__main__":
    # Print test cases
    print("Converting Celsius to Fahrenheit")
    for C in range(-100, 100, 5):
        print(str(C) + "C = " + str(c_to_f(C)) + "F")
    print("Converting Fahrenheit to Celsius")
    for F in range(-100, 100, 5):
        print(str(F) + "F = " + str(f_to_c(F)) + "C")
