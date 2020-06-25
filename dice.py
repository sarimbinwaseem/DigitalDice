
import random


def roll(numbers):

	rolled = [] 
	select = random.choice(numbers)
	# print(select)
	rolled.append(select)

	if select == 6:
		select2 = random.choice(numbers)
		# print(select2)
		rolled.append(select2)

		if select2 == 6:
			select3 = random.choice(numbers)
			# print(select3)
			rolled.append(select3)
			if select3 == 6:
				# print("Turn Dismissed")
				rolled = 0

	return rolled

def afterRoll(result):
	try:
		o = result[0]
	except:
		pass
	try:
		oo = result[1]
	except:
		pass
	try:
		ooo = result[2]
	except:
		pass

	if result == 0:
		t = f"Turn dismissed"
	elif len(result) == 3:
		t = f"{o} + {oo} + {ooo}"
	elif len(result) == 2:
		t = f"{o} + {oo}"
	elif len(result) == 1:
		t = f"{o}"

	return t

