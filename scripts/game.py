#!/usr/bin/env python3


import math
import random
from stringutils import compare_strings_withlog

class Game:
    def __init__(self):
        self.__secret = Game.string_generator() 

    @staticmethod
    def string_generator(size: int = 12):
        
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
        id = ''
        for i in range(0,size):
            id += random.choice(alpha)

        return id
    
    def check(self, answer):

        return compare_strings_withlog(self.__secret,answer)



if __name__ == '__main__':
    
    game = Game()
    print(game.check("123412341234"))
