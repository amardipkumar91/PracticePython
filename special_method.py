#----------------collection namedtuple---------------------------------
#---------- A deck as a sequence of cards.---------------------------

# import collections
# Card = collections.namedtuple('Card', ['rank', ' '])
# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA') 
#     suits = 'spades diamonds clubs hearts'.split()

#     def __init__(self):
#         self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#     def __len__(self):
#         return len(self._cards)
#     def __getitem__(self, position): 
#         return self._cards[position]

# beer_card = Card('7', 'diamonds')
# deck = FrenchDeck()

# suit_values = dict(spades=0, hearts=1, diamonds=2, clubs=3)

# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]

# for card in sorted(deck, key = spades_high):
#     print (card)

# ---- Vector class implementing the operations just described, through the use of the special methods __repr__, __abs__, __add__ and __mul__:---------

# from math import hypot
# class Vector:
#     def __init__(self, x =0 , y= 0):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return "Vector(%r, %r)"%(self.x, self.y)
    
#     def __abs__(self):
#         return hypot(self.x, self.y)

#     def __bool__(self):
#         return bool(abs(self))

#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#     def __mul__(self, scaler):
#         return Vector(self.x * scaler , self.y * scaler)
    
# obj = Vector(4,5)


#-----------------List Comprehension -------------------------

    


