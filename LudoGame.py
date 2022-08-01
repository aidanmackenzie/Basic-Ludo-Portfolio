# Author: Aidan MacKenzie
# GitHub username: aidanmackenzie
# Date: 07/31/2022
# Description: This code consists of a simplified game of Ludo. This game is made up of classes LudoGame and Player at
# a minimum. The player class contains at least the position the player chooses, the start and end space for the player,
# current position of their two tokens, and the current state of the player. It may contain additional information.
# Whereas the LudoGame object contains information about the players and information about the board.


class Board:
    """Represents the game board."""

    def __init__(self):
        self._general_board_spots = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [],
                                      '10': [], '11': [], '12': [], '13': [], '14': [], '15': [], '16': [], '17': [],
                                      '18': [], '19': [], '20': [], '21': [], '22': [], '23': [], '24': [], '25': [],
                                      '26': [], '27': [], '28': [], '29': [], '30': [], '31': [], '32': [], '33': [],
                                      '34': [], '35': [], '36': [], '37': [], '38': [], '39': [], '40': [], '41': [],
                                      '42': [], '43': [], '44': [], '45': [], '46': [], '47': [], '48': [], '49': [],
                                      '50': [], '51': [], '52': [], '53': [], '54': [], '55': [], '56': []}

        self._a_board_spots = {"H": [], "R": [], "A1": [], "A2": [], "A3": [], "A4": [], "A5": [], "A6": [], "E": []}
        self._b_board_spots = {"H": [], "R": [], "B1": [], "B2": [], "B3": [], "B4": [], "B5": [], "B6": [], "E": []}
        self._c_board_spots = {"H": [], "R": [], "C1": [], "C2": [], "C3": [], "C4": [], "C5": [], "C6": [], "E": []}
        self._d_board_spots = {"H": [], "R": [], "D1": [], "D2": [], "D3": [], "D4": [], "D5": [], "D6": [], "E": []}

    def get_general_board_spots(self):
        """Returns the general board spots and what is present on each."""
        return self._general_board_spots

    def get_a_board_spots(self):
        """Returns the unique board spots of player A and what is present on each."""
        return self._a_board_spots

    def get_b_board_spots(self):
        """Returns the unique board spots of player B and what is present on each."""
        return self._b_board_spots

    def get_c_board_spots(self):
        """Returns the unique board spots of player C and what is present on each."""
        return self._c_board_spots

    def get_d_board_spots(self):
        """Returns the unique board spots of player D and what is present on each."""
        return self._d_board_spots

    def general_add_token(self, spot_value, token_object):
        """Adds a token to a general board spot."""
        self._general_board_spots[spot_value].append(token_object)

    def a_add_token(self, spot_value, token_object):
        """Adds a token to an A player board spot."""
        if spot_value == "-1":
            self._a_board_spots["H"].append(token_object)

        elif spot_value == "0":
            self._a_board_spots["R"].append(token_object)

        elif spot_value == "57":
            self._a_board_spots["E"].append(token_object)

        else:
            inner_spot_value = f"A{spot_value - 50}"
            self._a_board_spots[inner_spot_value].append(token_object)

    def b_add_token(self, spot_value, token_object):
        """Adds a token to a B player board spot."""
        if spot_value == "-1":
            self._b_board_spots["H"].append(token_object)

        elif spot_value == "0":
            self._b_board_spots["R"].append(token_object)

        elif spot_value == "57":
            self._b_board_spots["E"].append(token_object)

        else:
            inner_spot_value = f"B{spot_value - 50}"
            self._b_board_spots[inner_spot_value].append(token_object)

    def c_add_token(self, spot_value, token_object):
        """Adds a token to a C player board spot."""
        if spot_value == "-1":
            self._c_board_spots["H"].append(token_object)

        elif spot_value == "0":
            self._c_board_spots["R"].append(token_object)

        elif spot_value == "57":
            self._c_board_spots["E"].append(token_object)

        else:
            inner_spot_value = f"C{spot_value - 50}"
            self._c_board_spots[inner_spot_value].append(token_object)

    def d_add_token(self, spot_value, token_object):
        """Adds a token to a D player board spot."""
        if spot_value == "-1":
            self._d_board_spots["H"].append(token_object)

        elif spot_value == "0":
            self._d_board_spots["R"].append(token_object)

        elif spot_value == "57":
            self._d_board_spots["E"].append(token_object)

        else:
            inner_spot_value = f"D{spot_value - 50}"
            self._d_board_spots[inner_spot_value].append(token_object)

    def general_remove_token(self, token_object):
        """Removes a token from a general board spot."""
        for key in self._general_board_spots:
            if token_object in self._general_board_spots[key]:
                self._general_board_spots[key].remove(token_object)

    def a_remove_token(self, token_object):
        """Removes a token from an A board spot"""
        for key in self._a_board_spots:
            if token_object in self._a_board_spots[key]:
                self._a_board_spots[key].remove(token_object)

    def b_remove_token(self, token_object):
        """Removes a token from a B board spot"""
        for key in self._b_board_spots:
            if token_object in self._b_board_spots[key]:
                self._b_board_spots[key].remove(token_object)

    def c_remove_token(self, token_object):
        """Removes a token from a C board spot"""
        for key in self._c_board_spots:
            if token_object in self._c_board_spots[key]:
                self._c_board_spots[key].remove(token_object)

    def d_remove_token(self, token_object):
        """Removes a token from a D board spot"""
        for key in self._d_board_spots:
            if token_object in self._d_board_spots[key]:
                self._d_board_spots[key].remove(token_object)


class Tokens:
    """Represents the player tokens."""
    def __init__(self, player_position, token_letter):




class Player:
    """Represents a player."""


class LudoGame:
    """Represents the game as played."""