import random


def roll(numbers: list) -> list:

	rolled = [] 
	selected = random.choice(numbers)
	# print(selected)
	rolled.append(selected)

	if rolled[0] == 6:
		rolled.append(random.choice(numbers))
	else:
		return rolled

	if rolled[1] == 6:
		rolled.append(random.choice(numbers))
	else:
		return rolled

	if rolled[2] == 6:
		rolled = [0]

	return rolled

def afterRoll(result: list) -> str:

	if result[0] == 0:
		t = f"Turn dismissed"
	else:
		t = " + ".join([str(r) for r in result])

	return t

