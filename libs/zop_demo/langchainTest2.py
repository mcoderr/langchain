from typing import overload

@overload
def square(x: int) -> int: ...

@overload
def square(x: float) -> float: ...

def square(x):
    return x * x


a = square(5)      # int
b = square(5.5)    # float

print(a)
print(b)
