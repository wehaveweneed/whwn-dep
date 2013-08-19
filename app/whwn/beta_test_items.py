from settings.common import project
import random

def beta_test_items():
	with open(project('whwn/test_items.txt')) as f:
		items = f.readlines()

		haves = random.sample(items, 5)
		items = set(items) - set(haves)
		needs = random.sample(items, 5)

	return {'haves': haves, 'needs': needs, "name": random.randint(0, 10000)}