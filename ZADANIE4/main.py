import functools


def licz_wywolania(funkcja):
    pass  # tu kod


@licz_wywolania
def kwadrat(x):
    return x * x


if __name__ == "__main__":
    print(kwadrat(3), kwadrat(x=4), kwadrat.wywolania)
