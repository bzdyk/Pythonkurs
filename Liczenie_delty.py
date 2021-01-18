import math


def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


a_str = input("wprowadz wspolczynnik a:")
b_str = input("wprowadz wspolczynnik b:")
c_str = input("wprowadz wspolczynnik C:")

print(check_int(a_str))

if not (check_int(a_str) and check_int(b_str) and check_int(c_str)):
    print("a, b and c need to be int!")




else:
    a = int(a_str)
    b = int(b_str)
    c = int(c_str)
    delta = (b * b) - (4 * a * c)
    print("delta: ", delta)

    if a == 0:
        print("to nie jest równanie kwadratowe")


    elif delta < 0:
        print("brak rozwiazania rownania")

    elif delta == 0:
        x1 = (-1 * b - delta) / 2 * a
        print(x1)

    else:
        x1 = ((-1 * b) - (math.sqrt(delta))) / (2 * a)
        x2 = ((-1 * b) + (math.sqrt(delta))) / (2 * a)
        print("x1: ", x1)
        print("x2: ", x2)



