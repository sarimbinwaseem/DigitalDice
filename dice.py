import random


def roll(numbers: list) -> list:

    rolled = []

    for _ in range(3):
        selected = random.choice(numbers)
        rolled.append(selected)
        if selected != 6:
            break

    # if all 3 are 6 so turn dismissed.
    if all([n == 6 for n in rolled]):
        return [0]

    return rolled


def afterRoll(result: list) -> str:

    if result[0] == 0:
        t = "Turn dismissed"
    else:
        t = " + ".join([str(r) for r in result])

    return t
