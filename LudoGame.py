# Author: Aidan MacKenzie
# GitHub username: aidanmackenzie
# Date: 07/31/2022
# Description: This code consists of a simplified game of Ludo. This game is made up of classes LudoGame and Player at
# a minimum. The player class contains at least the position the player chooses, the start and end space for the player,
# current position of their two tokens, and the current state of the player. It may contain additional information.
# Whereas the LudoGame object contains information about the players and information about the board.

class Tokens:
    """Represents the player tokens."""

    def __init__(self, token_name, player_position):
        """Creates a Tokens object."""
        self._token_name = token_name
        self._token_player_position = player_position

    def get_token_name(self):
        """Returns the token name, p or q."""
        return self._token_name

    def get_token_player_position(self):
        """Returns the player position of the token in question"""
        return self._token_player_position


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
        self._player_dict = {}
        self._final_token_locations = []

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
        if new_pos > 57:
            player_object.update_step_count(token_name, (57 - (new_pos - 57)))

        else:
            player_object.update_step_count(token_name, new_pos)


        if 0 < new_pos <= 56 and new_pos < 51:
            for player in self._player_dict.values():
                if player.get_space_name(player.get_token_p_step_count()) == player_object.get_space_name(
                        new_pos) and player.get_space_name(
                    player.get_token_q_step_count()) == player_object.get_space_name(
                    new_pos) and player != player_object:
                    player.update_step_count("p", -1)
                    player.update_step_count("q", -1)

                elif player.get_space_name(player.get_token_p_step_count()) == player_object.get_space_name(
                        new_pos) and player != player_object:
                    player.update_step_count("p", -1)

                elif player.get_space_name(player.get_token_q_step_count()) == player_object.get_space_name(
                        new_pos) and player != player_object:
                    player.update_step_count("q", -1)

        elif new_pos + int(player_object.get_start_pos()) - 1 >= 56 and new_pos < 51:
            for player in self._player_dict.values():
                if player.get_space_name(player.get_token_p_step_count()) == player_object.get_space_name(
                        new_pos) and player.get_space_name(
                    player.get_token_q_step_count()) == player_object.get_space_name(
                    new_pos) and player != player_object:
                    player.update_step_count("p", -1)

                    player.update_step_count("q", -1)

                elif player.get_space_name(player.get_token_p_step_count()) == player_object.get_space_name(
                        new_pos) and player != player_object:
                    player.update_step_count("p", -1)

                elif player.get_space_name(player.get_token_q_step_count()) == player_object.get_space_name(
                        new_pos) and player != player_object:
                    player.update_step_count("q", -1)

    def play_game(self, player_list, turn_list):
        """Plays the game of Ludo with the given player list and turn list."""
        for player in player_list:
            if player == "A":
                self._player_dict[player] = Player(player, "1", "50")

            elif player == "B":
                self._player_dict[player] = Player(player, "15", "8")

            elif player == "C":
                self._player_dict[player] = Player(player, "29", "22")

            elif player == "D":
                self._player_dict[player] = Player(player, "43", "36")

            else:
                print("Player position not available!")

        for turn in turn_list:
            if self._player_dict[turn[0]].get_token_p_step_count() == 57 and self._player_dict[turn[0]].get_token_q_step_count() == 57:
                continue

            else:
                if self._player_dict[turn[0]].get_token_p_step_count() == self._player_dict[turn[0]].get_token_q_step_count() and self._player_dict[turn[0]].get_token_p_step_count() >= 1:
                    self.move_token(self._player_dict[turn[0]], "p", turn[1])
                    self.move_token(self._player_dict[turn[0]], "q", turn[1])

                else:

                    if turn[1] == 6:
                        if self._player_dict[turn[0]].get_token_p_step_count() == -1 and self._player_dict[turn[0]].get_token_q_step_count() == -1:
                            self.move_token(self._player_dict[turn[0]], "p", 1)

                        elif self._player_dict[turn[0]].get_token_p_step_count() == -1 or self._player_dict[turn[0]].get_token_q_step_count() == -1:
                            if self._player_dict[turn[0]].get_token_p_step_count() == -1:
                                self.move_token(self._player_dict[turn[0]], "p", 1)
                            else:
                                self.move_token(self._player_dict[turn[0]], "q", 1)

                        else:
                            if self._player_dict[turn[0]].get_token_p_step_count() == 51:
                                self.move_token(self._player_dict[turn[0]], "p", 6)

                            elif self._player_dict[turn[0]].get_token_q_step_count() == 51:
                                self.move_token(self._player_dict[turn[0]], "q", 6)

                            elif self._player_dict[turn[0]].get_token_p_step_count() + turn[1] < 51 and self._player_dict[turn[0]].get_token_q_step_count() + turn[1] < 51:
                                current_filled = []
                                for player in self._player_dict.values():
                                    if player.get_player_position() == turn[0]:
                                        continue
                                    else:
                                        current_filled.append(player.get_space_name(player.get_token_p_step_count()))
                                        current_filled.append(player.get_space_name(player.get_token_q_step_count()))

                                if self._player_dict[turn[0]].get_space_name(self._player_dict[turn[0]].get_token_p_step_count() + turn[1]) in current_filled and self._player_dict[turn[0]].get_space_name(self._player_dict[turn[0]].get_token_q_step_count() + turn[1]) in current_filled:
                                    if self._player_dict[turn[0]].get_token_p_step_count() < self._player_dict[turn[0]].get_token_q_step_count():
                                        self.move_token(self._player_dict[turn[0]], "p", 6)

                                    else:
                                        self.move_token(self._player_dict[turn[0]], "q", 6)

                                elif self._player_dict[turn[0]].get_space_name(self._player_dict[turn[0]].get_token_p_step_count() + turn[1]) in current_filled:
                                    self.move_token(self._player_dict[turn[0]], "p", 6)

                                elif self._player_dict[turn[0]].get_space_name(self._player_dict[turn[0]].get_token_q_step_count() + turn[1]) in current_filled:
                                    self.move_token(self._player_dict[turn[0]], "q", 6)

                                else:
                                    if self._player_dict[turn[0]].get_token_p_step_count() < self._player_dict[
                                        turn[0]].get_token_q_step_count():
                                        self.move_token(self._player_dict[turn[0]], "p", 6)

                                    else:
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

                    elif self._player_dict[turn[0]].get_token_p_step_count() + turn[1] < 51 and self._player_dict[turn[0]].get_token_q_step_count() + turn[1] < 51:
                        local_current_filled = []
                        for player in self._player_dict.values():
                            if player.get_player_position() == turn[0]:
                                continue
                            else:
                                local_current_filled.append(player.get_space_name(player.get_token_p_step_count()))
                                local_current_filled.append(player.get_space_name(player.get_token_q_step_count()))

                        if self._player_dict[turn[0]].get_space_name(self._player_dict[turn[0]].get_token_p_step_count() + turn[1]) in local_current_filled and self._player_dict[turn[0]].get_space_name(self._player_dict[turn[0]].get_token_q_step_count() + turn[1]) in local_current_filled:
                            if self._player_dict[turn[0]].get_token_p_step_count() < self._player_dict[turn[0]].get_token_q_step_count():
                                self.move_token(self._player_dict[turn[0]], "p", turn[1])

                            else:
                                self.move_token(self._player_dict[turn[0]], "q", turn[1])

                        elif self._player_dict[turn[0]].get_space_name(self._player_dict[turn[0]].get_token_p_step_count() + turn[1]) in local_current_filled:
                            self.move_token(self._player_dict[turn[0]], "p", turn[1])

                        elif self._player_dict[turn[0]].get_space_name(self._player_dict[turn[0]].get_token_q_step_count() + turn[1]) in local_current_filled:
                            self.move_token(self._player_dict[turn[0]], "q", turn[1])

                        else:
                            if self._player_dict[turn[0]].get_token_p_step_count() < self._player_dict[turn[0]].get_token_q_step_count() and self._player_dict[turn[0]].get_token_p_step_count() >= 0:
                                self.move_token(self._player_dict[turn[0]], "p", turn[1])

                            elif self._player_dict[turn[0]].get_token_q_step_count() < self._player_dict[turn[0]].get_token_p_step_count() and self._player_dict[turn[0]].get_token_q_step_count() >= 0:
                                self.move_token(self._player_dict[turn[0]], "q", turn[1])

                            else:
                                self.move_token(self._player_dict[turn[0]], "p", turn[1])

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


#players = ['A', 'B']
#turns = [("A", 6), ("B", 6)]
#game = LudoGame()
#current_tokens_space = game.play_game(players, turns)
#player_A = game.get_player_by_position('A')
#print(current_tokens_space)
#print(player_A.get_completed())
#player_B = game.get_player_by_position('B')
#print(player_A.get_token_p_step_count())
#print(player_A.get_token_q_step_count())

players = ['A', 'B']
turns = [('A', 6), ('A', 6), ('A', 1), ('A', 4), ('A', 4), ('A', 6), ('B', 6), ('B', 6), ('B', 2), ('B', 2), ('A', 6)]
game = LudoGame()
current_tokens_space = game.play_game(players, turns)
player_A = game.get_player_by_position('A')
print(current_tokens_space)
player_B = game.get_player_by_position('B')

# Should return [5, 16, H, H]

#players = ['A','B','C','D']
#turns = [('A', 6),('A', 1),('B', 6),('B', 2),('C', 6),('C', 3),('D', 6),('D', 4)]
#game = LudoGame()
#current_tokens_space = game.play_game(players, turns)
#player_A = game.get_player_by_position('A')
#print(current_tokens_space)
#player_B = game.get_player_by_position('B')


#players = ['A','B']
#turns = [('A', 6), ("A", 4), ("A", 4), ("A", 4), ("A", 6), ("A", 5), ("A", 3), ("B", 6), ("B", 2), ("A", 2), ("A", 4)]
#game = LudoGame()
#current_tokens_space = game.play_game(players, turns)
#player_A = game.get_player_by_position('A')
#player_B = game.get_player_by_position('B')
#player_C = game.get_player_by_position('C')
#player_D = game.get_player_by_position('D')
#print(current_tokens_space)

# [('A', 6),('A', 4),('A', 4),('A', 4),('A', 6),('A', 5),('A', 3),('B', 6),('B', 2),('A', 2),('A', 4)]
# Should return [16, 10, H, H]
