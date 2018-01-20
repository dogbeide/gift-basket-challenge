from random import randint
from itertools import combinations
from copy import copy

'''
Generates a random list of 7 gifts.
Prepares best basket from 5 optimal gifts.
'''
class BasketWeaver(object):

    def __init__(self):
        # available criteria
        self.shapes = ['square', 'rectangle', 'circle','oval', 'triangle']
        self.weights = [50, 100, 150, 200, 250]
        self.seasons = ['winter', 'spring', 'summer', 'autumn']
        self.varieties = ['Perfect Variety (1)',
                          'Weight Variety (2)',
                          'Shape Variety (3)',
                          'Perfect Pairing (4)',
                          'Shape Pairing (5)',
                          'Discount Basket (6)']
        self.basket = [] # output list
        self.variety = None # basket type
        self.gifts = [] # input list

    def get_season(self):
        # input season
        season_index = int(input('What season is it? \n\
        (0 = winter, 1 = spring, 2 = summer, 3 = autumn): '))

        self.season = self.seasons[season_index]

    def get_gifts(self):

        # randomly generate 7 gifts
        for i in range(7):
            weight = self.weights[randint(0, 4)]
            shape = self.shapes[randint(0, 4)]
            self.gifts.append((weight, shape))

        # organize so larger weights will be picked first
        self.gifts = sorted(self.gifts, key=lambda g: g[0])[::-1]

    def make_basket(self):
        self.get_season() # get season from user
        self.get_gifts() # generate 7 gifts

        options = combinations(self.gifts, 5) # all possible gift baskets

        # check for basket 1 (perfect variety)?
        if self.season in ['winter', 'summer', 'autumn']:

            # check all potential (7 choose 5) baskets
            for option in options:
                weights = copy(self.weights)
                shapes = copy(self.shapes)

                # if both lists empty, perfection reached
                for gift in option:
                    if gift[0] in weights:
                        weights.remove(gift[0])
                    if gift[1] in shapes:
                        shapes.remove(gift[1])

                # 1 to 1 matchup, PERFECT variety found!
                if len(weights) == 0 and len(shapes) == 0:
                    self.basket = option
                    self.variety = 1
                    return

        # check for basket 2 (weight variety), then 3 (shape variety)
        if self.season in ['summer', 'autumn']:

            # weight?
            # check all potential (7 choose 5) baskets
            for option in options:
                weights = copy(self.weights)

                # if weights are empty, perfection reached
                for gift in option:
                    if gift[0] in weights:
                        weights.remove(gift[0])

                # 1 to 1 matchup, WEIGHT variety found!
                if len(weights) == 0:
                    self.basket = option
                    self.variety = 2
                    return


            # shape?
            # check all potential (7 choose 5) baskets
            for option in options:
                shapes = copy(self.shapes)

                # if weights are empty, perfection reached
                for gift in option:
                    if gift[1] in shapes:
                        shapes.remove(gift[1])

                # 1 to 1 matchup, SHAPE variety found!
                if len(shapes) == 0:
                    self.basket = option
                    self.variety = 3
                    return


        # check for basket 4 (perfect pairing)
        if self.season in ['winter', 'spring', 'summer']:
            #TODO:
            pass


        #check for basket 5 (shape pairing)
        if self.season in ['spring', 'summer']:
            #TODO:
            pass


        # default basket 6, top 5 heaviest gifts
        # avoid re-referencing (assume shared API, distinction)
        self.basket = copy(self.gifts)[:5]
        self.variety = 6


    def display_result(self):
        # neatly display all results
        print('')
        print(self.varieties[self.variety-1]+': ')
        for gift in self.basket:
            print('\t' + str(gift))



bw = BasketWeaver()
bw.make_basket()
bw.display_result()
