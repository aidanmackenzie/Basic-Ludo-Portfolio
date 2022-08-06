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
        """Creates a game board."""
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
            inner_spot_value = f"A{int(spot_value) - 50}"
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
            inner_spot_value = f"B{int(spot_value) - 50}"
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
            inner_spot_value = f"C{int(spot_value) - 50}"
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
            inner_spot_value = f"D{int(spot_value) - 50}"
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

    def __init__(self, token_name, player_position):
        """Creates a Tokens object."""
        self._token_name = token_name
        self._token_player_position = player_position
        self._token_location = "-1"

    def get_token_name(self):
        """Returns the token name, p or q."""
        return self._token_name

    def get_token_player_position(self):
        """Returns the player position of the token in question"""
        return self._token_player_position

    def get_token_location(self):
        """Returns the token's location as a string of an integer ranging from -1 to 57."""
        return self._token_location

    def update_token_location(self, new_location):
        """Shifts token location to new value."""
        self._token_location = new_location


class Player:
    """Represents a player."""

    def __init__(self, player_position, start_pos, end_pos):
        """Creates a player object."""
        self._player_tokens = [Tokens('p', player_position), Tokens('q', player_position)]
        self._player_position = player_position
        self._start_pos = start_pos
        self._end_pos = end_pos
        self._token_p_step_count = -1
        self._token_q_step_count = -1
        self._completed = False

    def get_player_position(self):
        """Returns the player's position."""
        return self._player_position

    def get_player_tokens(self):
        """Returns the players token objects."""
        return self._player_tokens

    def get_token_p_step_count(self):
        """Returns the total steps that token p has taken."""
        return self._token_p_step_count

    def get_token_q_step_count(self):
        """Returns the total steps that token q has taken."""
        return self._token_q_step_count

    def update_step_count(self, token_name, new_step_count):
        """Updates the step count of the appropriate token."""
        if token_name == "p":
            self._token_p_step_count = new_step_count

        elif token_name == "q":
            self._token_q_step_count = new_step_count

    def get_completed(self):
        """Returns True if player has finished game, False otherwise."""
        if self._token_q_step_count == 57 and self._token_p_step_count == 57:
            return True

        else:
            return False

    def get_start_pos(self):
        """Returns the player's start position."""
        return self._start_pos

    def get_space_name(self, total_steps):
        """Returns the name of the space the token with given step count has landed on."""
        if str(total_steps) == "-1":
            return "H"

        elif str(total_steps) == "0":
            return "R"

        elif str(total_steps) == "57":
            return "E"

        elif 50 < total_steps < 57:
            return f"{self._player_position}{total_steps - 50}"

        elif total_steps + int(self._start_pos) - 57 == 0:
            return "56"

        elif total_steps + int(self._start_pos) >= 57:
            return f"{(total_steps + int(self._start_pos)) - 57}"

        else:
            return f"{total_steps + int(self._start_pos) - 1}"


class LudoGame:
    """Represents the game as played."""

    def __init__(self):
        """Creates a LudoGame object."""
        self._board = Board()
        self._player_dict = {}
        self._final_token_locations = []

    def get_board(self):
        """Returns the game board for current game."""
        return self._board

    def get_player_dict(self):
        """Returns the player list for the current game."""
        return self._player_dict

    def get_player_by_position(self, letter_position):
        """Returns the player object linked to the position, if player not an option, returns that player not found."""
        if "D" < letter_position or letter_position < "A":
            return "Player not found!"

        else:
            if letter_position in self._player_dict:
                return self._player_dict[letter_position]

            else:
                return "Player not found!"

    def move_token(self, player_object, token_name, steps_to_take_int):
        """Moves a player's token from initial spot to new spot based on their 'roll'."""
        original_pos = None
        if token_name == "p":
            original_pos = player_object.get_token_p_step_count()

        elif token_name == "q":
            original_pos = player_object.get_token_q_step_count()

        new_pos = original_pos + steps_to_take_int

        for token in player_object.get_player_tokens():
            if token.get_token_name() == token_name:
                if 1 <= int(token.get_token_location()) <= 50:
                    self._board.general_remove_token(token)
                    if new_pos == -1:
                        if player_object.get_player_position == "A":
                            self._board.a_add_token("-1", token)

                        elif player_object.get_player_position == "B":
                            self._board.b_add_token("-1", token)

                        elif player_object.get_player_position == "C":
                            self._board.c_add_token("-1", token)

                        elif player_object.get_player_position == "D":
                            self._board.d_add_token("-1", token)

                    elif new_pos == 0:
                        if player_object.get_player_position == "A":
                            self._board.a_add_token("0", token)

                        elif player_object.get_player_position == "B":
                            self._board.b_add_token("0", token)

                        elif player_object.get_player_position == "C":
                            self._board.c_add_token("0", token)

                        elif player_object.get_player_position == "D":
                            self._board.d_add_token("0", token)

                    elif 0 < new_pos + int(player_object.get_start_pos()) <= 56 and new_pos < 51:
                        self._board.general_add_token(f"{new_pos + int(player_object.get_start_pos())}", token)

                    elif new_pos + int(player_object.get_start_pos()) > 56 and new_pos < 51:
                        self._board.general_add_token(f"{new_pos - (57 - int(player_object.get_start_pos()))}", token)

                    elif 57 > new_pos >= 51:
                        if player_object.get_player_position == "A":
                            self._board.a_add_token(f"A{new_pos - 50}", token)

                        elif player_object.get_player_position == "B":
                            self._board.b_add_token(f"B{new_pos - 50}", token)

                        elif player_object.get_player_position == "B":
                            self._board.b_add_token(f"B{new_pos - 50}", token)

                        elif player_object.get_player_position == "C":
                            self._board.c_add_token(f"C{new_pos - 50}", token)

                        elif player_object.get_player_position == "D":
                            self._board.d_add_token(f"D{new_pos - 50}", token)

                else:
                    if player_object.get_player_position == "A":
                        self._board.a_remove_token(token)
                        if new_pos == -1:
                            self._board.a_add_token("-1", token)

                        elif new_pos == 0:
                            self._board.a_add_token("0", token)

                        elif 0 < new_pos + int(player_object.get_start_pos()) - 1 <= 56 and new_pos < 51:
                            self._board.general_add_token(f"{new_pos + int(player_object.get_start_pos()) - 1}", token)

                        elif new_pos + int(player_object.get_start_pos()) - 1 >= 56 and new_pos < 51:
                            self._board.general_add_token(f"{new_pos - (57 - int(player_object.get_start_pos()))}", token)

                        elif 51 <= new_pos <= 57 or new_pos == -1 or new_pos == 0:
                            self._board.a_add_token(new_pos, token)

                        elif new_pos > 57:
                            bounce_pos = str(57 - (new_pos - 57))
                            new_pos = bounce_pos
                            self._board.a_add_token(new_pos, token)

                    elif player_object.get_player_position == "B":
                        self._board.b_remove_token(token)
                        if new_pos == -1:
                            self._board.b_add_token("-1", token)

                        elif new_pos == 0:
                            self._board.b_add_token("0", token)

                        elif 0 < new_pos + int(player_object.get_start_pos()) - 1 <= 56 and new_pos < 51:
                            self._board.general_add_token(f"{new_pos + int(player_object.get_start_pos()) - 1}", token)

                        elif new_pos + int(player_object.get_start_pos()) - 1 >= 56 and new_pos < 51:
                            self._board.general_add_token(f"{new_pos - (57 - int(player_object.get_start_pos()))}", token)

                        elif 51 <= new_pos <= 57 or new_pos == -1 or new_pos == 0:
                            self._board.b_add_token(new_pos, token)

                        elif new_pos > 57:
                            bounce_pos = str(57 - (new_pos - 57))
                            new_pos = bounce_pos
                            self._board.b_add_token(new_pos, token)

                    elif player_object.get_player_position == "C":
                        self._board.c_remove_token(token)
                        if new_pos == -1:
                            self._board.c_add_token("-1", token)

                        elif new_pos == 0:
                            self._board.c_add_token("0", token)

                        elif 0 < new_pos + int(player_object.get_start_pos()) - 1 <= 56 and new_pos < 51:
                            self._board.general_add_token(f"{new_pos + int(player_object.get_start_pos()) - 1}", token)

                        elif new_pos + int(player_object.get_start_pos()) - 1 >= 56 and new_pos < 51:
                            self._board.general_add_token(f"{new_pos - (57 - int(player_object.get_start_pos()))}", token)

                        elif 51 <= new_pos <= 57 or new_pos == -1 or new_pos == 0:
                            self._board.c_add_token(new_pos, token)

                        elif new_pos > 57:
                            bounce_pos = str(57 - (new_pos - 57))
                            new_pos = bounce_pos
                            self._board.c_add_token(new_pos, token)

                    elif player_object.get_player_position == "D":
                        self._board.d_remove_token(token)
                        if new_pos == -1:
                            self._board.d_add_token("-1", token)

                        elif new_pos == 0:
                            self._board.d_add_token("0", token)

                        elif 0 < new_pos + int(player_object.get_start_pos()) - 1 <= 56 and new_pos < 51:
                            self._board.general_add_token(f"{new_pos + int(player_object.get_start_pos()) - 1}", token)

                        elif new_pos + int(player_object.get_start_pos()) - 1 >= 56 and new_pos < 51:
                            self._board.general_add_token(f"{new_pos - (57 - int(player_object.get_start_pos()))}", token)

                        elif 51 <= new_pos <= 57 or new_pos == -1 or new_pos == 0:
                            self._board.d_add_token(new_pos, token)

                        elif new_pos > 57:
                            bounce_pos = str(57 - (new_pos - 57))
                            new_pos = bounce_pos
                            self._board.d_add_token(new_pos, token)

                token.update_token_location(str(new_pos))
                player_object.update_step_count(token_name, new_pos)

                if 0 < new_pos + int(player_object.get_start_pos()) - 1 <= 56 and new_pos < 51:
                    for player in self._player_dict.values():
                        if player.get_space_name(player.get_token_p_step_count()) == player_object.get_space_name(
                                new_pos) and player.get_space_name(
                            player.get_token_q_step_count()) == player_object.get_space_name(
                            new_pos) and player != player_object:
                            player.update_step_count("p", -1)
                            player.get_player_tokens()[0].update_token_location("-1")
                            player.update_step_count("q", -1)
                            player.get_player_tokens()[1].update_token_location("-1")

                        elif player.get_space_name(player.get_token_p_step_count()) == player_object.get_space_name(
                                new_pos) and player != player_object:
                            player.update_step_count("p", -1)
                            player.get_player_tokens()[0].update_token_location("-1")

                        elif player.get_space_name(player.get_token_q_step_count()) == player_object.get_space_name(
                                new_pos) and player != player_object:
                            player.update_step_count("q", -1)
                            player.get_player_tokens()[1].update_token_location("-1")



                elif new_pos + int(player_object.get_start_pos()) - 1 >= 56 and new_pos < 51:
                    for player in self._player_dict.values():
                        if player.get_space_name(player.get_token_p_step_count()) == player_object.get_space_name(
                                new_pos) and player.get_space_name(
                            player.get_token_q_step_count()) == player_object.get_space_name(
                            new_pos) and player != player_object:
                            player.update_step_count("p", -1)
                            player.get_player_tokens()[0].update_token_location("-1")
                            player.update_step_count("q", -1)
                            player.get_player_tokens()[1].update_token_location("-1")

                        elif player.get_space_name(player.get_token_p_step_count()) == player_object.get_space_name(
                                new_pos) and player != player_object:
                            player.update_step_count("p", -1)
                            player.get_player_tokens()[0].update_token_location("-1")

                        elif player.get_space_name(player.get_token_q_step_count()) == player_object.get_space_name(
                                new_pos) and player != player_object:
                            player.update_step_count("q", -1)
                            player.get_player_tokens()[1].update_token_location("-1")


    def play_game(self, player_list, turn_list):
        """Plays the game of Ludo with the given player list and turn list."""
        for player in player_list:
            if player == "A":
                self._player_dict[player] = Player(player, "1", "50")
                self._board.a_add_token("-1", self._player_dict["A"].get_player_tokens()[0])
                self._board.a_add_token("-1", self._player_dict["A"].get_player_tokens()[1])

            elif player == "B":
                self._player_dict[player] = Player(player, "15", "8")
                self._board.b_add_token("-1", self._player_dict["B"].get_player_tokens()[0])
                self._board.b_add_token("-1", self._player_dict["B"].get_player_tokens()[1])

            elif player == "C":
                self._player_dict[player] = Player(player, "29", "22")
                self._board.c_add_token("-1", self._player_dict["C"].get_player_tokens()[0])
                self._board.c_add_token("-1", self._player_dict["C"].get_player_tokens()[1])

            elif player == "D":
                self._player_dict[player] = Player(player, "43", "36")
                self._board.c_add_token("-1", self._player_dict["A"].get_player_tokens()[0])
                self._board.c_add_token("-1", self._player_dict["A"].get_player_tokens()[1])

            else:
                print("Player position not available!")

        for turn in turn_list:
            if self._player_dict[turn[0]].get_token_p_step_count() == 57 and self._player_dict[turn[0]].get_token_q_step_count() == 57:
                return

            else:
                if self._player_dict[turn[0]].get_token_p_step_count() == self._player_dict[turn[0]].get_token_q_step_count() and self._player_dict[turn[0]].get_token_p_step_count() >= 1:
                    self.move_token(self._player_dict[turn[0]], "p", turn[1])
                    self.move_token(self._player_dict[turn[0]], "q", turn[1])

                else:

                    if turn[1] == 6:
                        if self._player_dict[turn[0]].get_token_p_step_count() == -1 and self._player_dict[turn[0]].get_token_q_step_count() == -1:
                            self.move_token(self._player_dict[turn[0]], "p", 1)

                        elif self._player_dict[turn[0]].get_token_p_step_count() == -1:
                            self.move_token(self._player_dict[turn[0]], "p", 1)

                        elif self._player_dict[turn[0]].get_token_q_step_count() == -1:
                            self.move_token(self._player_dict[turn[0]], "q", 1)

                        else:
                            if self._player_dict[turn[0]].get_token_p_step_count() == 51:
                                self.move_token(self._player_dict[turn[0]], "p", 6)

                            elif self._player_dict[turn[0]].get_token_q_step_count() == 51:
                                self.move_token(self._player_dict[turn[0]], "q", 6)

                            else:
                                if self._player_dict[turn[0]].get_token_p_step_count() < self._player_dict[turn[0]].get_token_q_step_count():
                                    self.move_token(self._player_dict[turn[0]], "p", 6)

                                else:
                                    self.move_token(self._player_dict[turn[0]], "q", 6)

                    elif str(self._player_dict[turn[0]].get_token_p_step_count() + turn[1]) == "57" or str(self._player_dict[turn[0]].get_token_q_step_count() + turn[1]) == "57":
                        if str(self._player_dict[turn[0]].get_token_p_step_count() + turn[1]) == "57":
                            self.move_token(self._player_dict[turn[0]], "p", turn[1])

                        elif str(self._player_dict[turn[0]].get_token_q_step_count() + turn[1]) == "57":
                            self.move_token(self._player_dict[turn[0]], "q", turn[1])

                    elif self._player_dict[turn[0]].get_token_p_step_count() < self._player_dict[turn[0]].get_token_q_step_count() and self._player_dict[turn[0]].get_token_p_step_count() >= 0:
                        self.move_token(self._player_dict[turn[0]], "p", turn[1])

                    elif self._player_dict[turn[0]].get_token_q_step_count() < self._player_dict[turn[0]].get_token_p_step_count() and self._player_dict[turn[0]].get_token_q_step_count() >= 0:
                        self.move_token(self._player_dict[turn[0]], "q", turn[1])

                    else:
                        self.move_token(self._player_dict[turn[0]], "p", turn[1])

        for player in self._player_dict.values():
            self._final_token_locations.append(player.get_space_name(player.get_token_p_step_count()))
            self._final_token_locations.append(player.get_space_name(player.get_token_q_step_count()))

        return self._final_token_locations


players = ['A', 'B']
turns = [('A', 6), ('A', 4), ('A', 5), ('A', 4), ('B', 6), ('B', 4), ('B', 1), ('B', 2), ('A', 6), ('A', 4), ('A', 6), ('A', 3), ('A', 5), ('A', 1), ('A', 5), ('A', 4)]
game = LudoGame()
current_tokens_space = game.play_game(players, turns)
player_A = game.get_player_by_position('A')
print(player_A.get_completed())
print(player_A.get_token_p_step_count())
print(current_tokens_space)
player_B = game.get_player_by_position('B')
print(player_B.get_space_name(55))

