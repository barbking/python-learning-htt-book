# Barbara King

# H8-3: pokerodds2.py
#
#   Starting code H8-3
#
# start with your pokerodds.py code from Lab 9 (L9-4)
#

import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]


class Card():
    """
    Represents a single playing card,
        whose rank internally is int _rank: 1..13 => "Ace".."King"
        and whose suit internally is int _suit 0..3 => "Clubs".."Spades"
    """

    def __init__(self, rank=1, suit=3):
        '''
        Initialize card with given int suit and int rank
        :param rank:
        :param suit:
        :return:
        '''
        self._rank = rank
        self._suit = suit

    def __str__(self):
        '''
        Return the string name of this card:
        "Ace of Spades": translates int fields to strings
        :return:
        '''

        # "Ace of Spades" is string for self._rank==1, self._suit==3

        toreturn = RANKS[self._rank] + " of " + SUITS[self._suit]

        return toreturn


class Deck():
    """
    Represents a deck of 52 standard playing cards,
        as a list of Card refs
    """

    def __init__(self):
        '''
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        :return: nothing
        '''

        self._cards = []
        for rank in range(1, 14):
            for suit in range(4):
                c = Card(rank, suit)
                self._cards.append(c)

    def __str__(self):
        '''
        "Stringified" deck: string of Card named,
        with \n for easier reading
        :return:
        '''
        toreturn = ''

        # for index in range(len(self._cards)):
        #     self._cards[index]

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            toreturn = toreturn + temp + "\n"  # note \n at end

        return toreturn

    def shuffle(self):
        random.shuffle(self._cards)  # note random function to do this

    def dealCard(self):
        toreturn = self._cards.pop(0)  # get and remove top card from deck
        return toreturn


def buildDict(hand):
    dict = {}

    for card in hand:
        dict[card._rank] = dict.get(card._rank, 0) + 1  # same as if loop

    # print(dict)
    return dict


def buildSuitDict(hand):
    suitdict = {}  # added to keep track of suits
    for card in hand:
        suit = (SUITS[card._suit])
        suitdict[suit] = suitdict.get(suit, 0) + 1
    return suitdict


def hasOnePair(dict):
    # Check for EXACTLY one value of 2 in dict
    # Note there might be 2 pairs; hence the counting of pairs

    # HOWEVER: there's a problem with this code, as it counts
    #   some hands as having 1 pair when they're not.
    # Hint: Bob Saget... (obscure TV trivia reference)

    twocount = 0
    threecount = 0
    for v in dict.values():
        if v == 2:
            twocount += 1
        elif v == 3:
            threecount += 1

    return twocount == 1 and threecount != 1


def hasTwoPairs(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''
    twocount = 0
    fourcount = 0
    for v in dict.values():
        if v == 2:
            twocount += 1
        elif v == 4:
            fourcount += 1

    return twocount == 2 and fourcount != 1


def hasThreeOfAKind(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''

    twocount = 0
    threecount = 0
    for v in dict.values():
        if v == 3:
            threecount += 1
        elif v == 2:
            twocount += 1

    return threecount == 1 and twocount != 1


def hasFullHouse(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''
    twocount = 0
    threecount = 0
    fullHouseCount = 0
    for v in dict.values():
        if v == 3:
            threecount += 1
        elif v == 2:
            twocount += 1
    if twocount == 1 and threecount == 1:
        fullHouseCount = 1
    return fullHouseCount == 1

def hasFourOfAKind(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''

    fourcount = 0
    for v in dict.values():
        if v == 4:
            fourcount += 1
    return fourcount == 1


def hasStraight(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''

    return False


def hasFlush(suitdict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''
    fivecount = 0
    for v in suitdict.values():
        if v == 5:
            fivecount += 1
    return fivecount == 1


def hasStraightFlush(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''

    return False


def hasRoyalFlush(dict):
    '''
    Complete this!
    :param dict: dictionary with card ranks to check
    '''

    return False


def main():
    # finish this...

    TRIALS = 10000  # int(input ("Input number of hands to test: "))

    hand = []  # list of Card in hand

    # accumulators for different counts

    onepairCount = 0
    twopairCount = 0
    threeCount = 0
    fourCount = 0
    fullHouseCount = 0

    # more if you wish...

    for num in range(TRIALS):

        d = Deck()
        d.shuffle()
        hand = []

        for count in range(5):
            hand.append(d.dealCard())

        dict = buildDict(hand)
        suitdict = buildSuitDict(hand)

        if hasOnePair(dict):
            onepairCount += 1
        elif hasTwoPairs(dict):
            twopairCount += 1
        elif hasThreeOfAKind(dict):
            threeCount += 1
        elif hasFourOfAKind(dict):
            fourCount += 1
        elif hasFullHouse(dict):
            fullHouseCount += 1

        # add more if you wish...

    # print out results...

    print("Number of one pair hands is: ", onepairCount)
    print("% of hands: ", 100.0 * onepairCount / TRIALS)

    print("Number of two pair hand is: ", twopairCount)
    print("% of hands: ", 100.0 * twopairCount / TRIALS)

    print("Number of three of a kind: ", threeCount)
    print("% of hands: ", 100.0 * threeCount / TRIALS)

    print("Number of four of a kind: ", fourCount)
    print("% of hands: ", 100.0 * fourCount / TRIALS)

    print("Number of full house: ", fullHouseCount)
    print("% of hands: ", 100.0 * fullHouseCount/ TRIALS)

def test():
    ''' hardcoded hand, allowing test of hasXXX() methods
    '''

    testhand = [Card(1, 3), Card(11, 3), \
                Card(1, 3), Card(11, 3), \
                Card(12, 3)]
    # here's a hand that seems to have one pair; does it?

    # testhand = [Card(2, 3), Card(1, 2), \
    #             Card(1, 1), Card(1, 3), \
    #             Card(2, 0)]

    dict = buildDict(testhand)
    suitdict = buildSuitDict(testhand)

    print("Does handtest contain exactly one pair? %s" % hasOnePair(dict))
    print("Does handtest contain exactly two pair? %s" % hasTwoPairs(dict))
    print("Does handtest contain three of a kind? %s" % hasThreeOfAKind(dict))
    print("Does handtest contain four of a kind? %s" % hasFourOfAKind(dict))
    print("Does handtest contain a full house? %s" % hasFullHouse(dict))
    print("Does handtest contain a flush? %s" % hasFlush(suitdict))


def testCard():
    card1 = Card(1, 3)
    card2 = Card(12, 2)
    card1._newfield = 47

    print(card1.__str__())  # long-winded form
    print(str(card2))
    print(card1._newfield)
    print(card1._rank)
    print("suit:", card1._suit)


def testDeck():
    '''
    Test Deck: create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    '''
    deck = Deck()
    print(str(deck))

    print("Now we shuffle:\n")

    deck.shuffle()
    print(str(deck))

    c = deck.dealCard()

    c2 = deck.dealCard()

    print("The first card dealt is", str(c), "and the second is", str(c2))
    print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!


if __name__ == "__main__":
    #     testCard()  # uncomment to test creating & calling Card methods

    #     testDeck()  # uncomment to test Deck: create, print, shuffle, print

    # test()  # uncomment to test hand (list of 5 Card obj) for one pair

    main()  # uncomment to run general poker odds calculations
