# Author: Aidan MacKenzie
# GitHub username: aidanmackenzie
# Date: 07/31/2022
# Description: This code consists of a simplified game of Ludo. This game is made up of classes LudoGame and Player at
# a minimum. The player class contains at least the position the player chooses, the start and end space for the player,
# current position of their two tokens, and the current state of the player. It may contain additional information.
# Whereas the LudoGame object contains information about the players and information about the board.

class Board:
    """Represents the gameboard."""

    def __init__(self):
        self._general_board_spots = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [],
                                      '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [],
                                      '18': [], '19': [], '20': [], '21': [], '22': [], '23': [], '24': [], '25': [],
                                      '26': [], '27': [], '28': [], '29': [], '30': [], '31': [], '32': [], '33': [],
                                      '34': [], '35': [], '36': [], '37': [], '38': [], '39': [], '40': [], '41': [],
                                      '42': [], '43': [], '44': [], '45': [], '46': [], '47': [], '48': [], '49': [],
                                      '50': [], '51': [], '52': [], '53': [], '54': [], '55': [], '56': []}

        self._a_board_spots = {"A1": [], "A2": [], "A3": [], "A4": [], "A5": [], "A6": []}
        self._b_board_spots = {"B1": [], "B2": [], "B3": [], "B4": [], "B5": [], "B6": []}
        self._c_board_spots = {"C1": [], "C2": [], "C3": [], "C4": [], "C5": [], "C6": []}
        self._d_board_spots = {"D1": [], "D2": [], "D3": [], "D4": [], "D5": [], "D6": []}
        self._winning_spot = {"E": []}