import random


def roll(numbers):

	rolled = [] 
	selected = random.choice(numbers)
	# print(selected)
	rolled.append(selected)

	if selected == 6:
		selected2 = random.choice(numbers)
		# print(selected2)
		rolled.append(selected2)

		if selected2 == 6:
			selected3 = random.choice(numbers)
			# print(selected3)
			rolled.append(selected3)
			if selected3 == 6:
				# print("Turn Dismissed")
				rolled = 0

	return rolled

def afterRoll(result):

	if result == 0:
		t = f"Turn dismissed"
	else:
		t = " + ".join([str(r) for r in result])

	return t

