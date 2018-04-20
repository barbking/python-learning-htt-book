'''
Barbara King
test_pokerodds.py:

py.test unit test to check for one pair
'''

import pokerodds2 as p

def test_one_pair():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(3, 1), p.Card(13, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasOnePair(dict)

def test_one_pair_2():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(3, 1), p.Card(13, 2), \
				p.Card(12, 0)]

	dict = p.buildDict(testhand)

	assert not p.hasOnePair(dict)

def test_one_pair_3():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(13, 2), \
				p.Card(13, 0)]

	dict = p.buildDict(testhand)

	assert not p.hasOnePair(dict)

def test_two_pairs():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(13, 1), p.Card(13, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasTwoPairs(dict)

def test_two_pairs_2():

	testhand = [p.Card(2, 3), p.Card(2, 2), \
				p.Card(2, 1), p.Card(13, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert not p.hasTwoPairs(dict)

def test_two_pairs_3():
	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(1, 0), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert not p.hasTwoPairs(dict)

def test_ThreeOfAKind():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(13, 1), p.Card(2, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasThreeOfAKind(dict)

def test_ThreeOfAKind_2():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(1, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert not p.hasThreeOfAKind(dict)

def test_ThreeOfAKind_3():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(13, 2), \
				p.Card(4, 0)]

	dict = p.buildDict(testhand)

	assert not p.hasThreeOfAKind(dict)

def test_FourOfAKind():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(2, 2), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasFourOfAKind(dict)

def test_FourOfAKind_2():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(2, 2), \
				p.Card(12, 0)]

	dict = p.buildDict(testhand)

	assert not p.hasFourOfAKind(dict)

def test_FourOfAKind_3():

	testhand = [p.Card(12, 3), p.Card(1, 2), \
				p.Card(12, 1), p.Card(12, 2), \
				p.Card(12, 0)]

	dict = p.buildDict(testhand)

	assert p.hasFourOfAKind(dict)

def test_FullHouse():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(1, 0), \
				p.Card(2, 0)]

	dict = p.buildDict(testhand)

	assert p.hasFullHouse(dict)

def test_FullHouse_2():

	testhand = [p.Card(2, 3), p.Card(1, 2), \
				p.Card(2, 1), p.Card(1, 0), \
				p.Card(12, 0)]

	dict = p.buildDict(testhand)

	assert not p.hasFullHouse(dict)

def test_FullHouse_3():

	testhand = [p.Card(12, 3), p.Card(1, 2), \
				p.Card(12, 1), p.Card(1, 0), \
				p.Card(1, 0)]

	dict = p.buildDict(testhand)

	assert p.hasFullHouse(dict)