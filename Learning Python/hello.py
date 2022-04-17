import numpy as np
from functools import partial

x = np.array([12, 43, 2, 100, 54, 5, 68])

def display_arguments(a, b):
    print(f"a --> {a}")
    print(f"b --> {b}")

display_arguments(10, 20)

display_argument_fixedA = partial(display_arguments, a=70)
display_argument_fixedB = partial(display_arguments, b=100)
display_argument_fixedA(b=30)
display_argument_fixedB(a=200)
