#!usr/bin/env python
# -*- coding: utf-8 -*-
"""A Pig Dice Game."""


import random


class Game(object):
    """constructor for a two player.

    Attributes: None
    """

    def __init__(self, players):
        self.players = players
        self.player_index = {n: Player(n) for n in self.players}
        self.scores = {n: 0 for n in self.players}
        self.max_score = 100
        self.high_score = 0
        self.starter = None
        self.next_player = None
        self.toss()

        while self.max_score > self.high_score:
            print '\n'
            print '\n'
            print '-' * 40
            print '{}, your score is {}.'.format(self.next_player, self.scores[self.next_player])
            print '\n'
            print 'It is now {}, turn to roll: '.format(self.starter)
            print '{}, your score is {}.'.format(self.starter, self.scores[self.starter])
            choice = raw_input(
                'Do you want to roll or hold? ( r or h ): ').lower()
            if choice == 'r':
                rolled = self.player_index[self.starter].throw()
                total = self.scores[self.starter] + \
                    self.player_index[self.starter].turn_score
                round_score = self.player_index[self.starter].turn_score
                plyr_score = self.scores[self.starter]
                name = self.starter
                if rolled == 1:
                    print '*' * 40
                    print 'You rolled a 1 and loose all points in round.'
                    print '*' * 40
                    self.turn_score = 0
                    self.turn_pass()
                    print '{} your score is {}.'.format(name, plyr_score)
                    continue
                elif total > self.max_score:
                    print '{} lost your score is {}.'.format(name, total)
                    break
                else:
                    print '{} You rolled {}, and round score is {}.'.format(name, rolled, round_score)
                    print '\n'
                    print 'If you hold your score will be {}'.format(total)
            elif choice == 'h':
                plyr_score = self.scores[self.starter]
                name = self.starter
                total = plyr_score + self.player_index[self.starter].turn_score
                if total == self.max_score:
                    print '{} is the winner with score of {}.'.format(name, 100)
                    break
                elif total > self.max_score:
                    print '{} you have lost, with score of {}.'.format(self.starter, total)
                    break
                else:
                    self.scores[self.starter] = total
                    self.player_index[self.starter].turn_score = 0
                    self.player_index[self.starter].turn = False
                    self.turn_pass()
            else:
                continue

    def toss(self):
        """A function sets first, second player.

        Attribute: none
        """
        toss = random.choice(self.players)
        toss = self.players.index(toss)
        if toss == 0:
            self.starter = self.players[0]
            self.next_player = self.players[1]
        else:
            self.starter = self.players[1]
            self.next_player = self.players[0]

    def turn(self):
        pass

    def turn_pass(self):
        hold_player = self.starter
        self.starter = self.next_player
        self.next_player = hold_player


class Player(object):
    """Players turn at rolling.

    Attributes: None
    """

    def __init__(self, name):
        self.name = ''
        self.turn_score = 0
        self.turn = True

    def throw(self):
        """returns number rolled.

        Attribute: None
        """
        die = Die()
        rolled = die.roll()
        if rolled != 1:
            self.turn_score += rolled
        else:
            self.turn_score = 0
            self.turn = False
        return rolled


class Die(object):
    """A constructor.

    Attributes: None
    """

    def __init__(self):
        self.rolled = 0

    def roll(self):
        """roll function returns number.

        Attribute: None
        """
        self.rolled = random.choice(range(1, 7))
        return self.rolled


if __name__ == '__main__':
    pig = Game(['Player1', 'Player2'])
