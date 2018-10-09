""" Where's That Word? functions. """

# The constant describing the valid directions. These should be used
# in functions get_factor and check_guess.
UP = 'up'
DOWN = 'down'
FORWARD = 'forward'
BACKWARD = 'backward'

# The constants describing the multiplicative factor for finding a
# word in a particular direction.  This should be used in get_factor.
FORWARD_FACTOR = 1
DOWN_FACTOR = 2
BACKWARD_FACTOR = 3
UP_FACTOR = 4

# The constant describing the threshold for scoring. This should be
# used in get_points.
THRESHOLD = 5
BONUS = 12

# The constants describing two players and the result of the
# game. These should be used as return values in get_current_player
# and get_winner.
P1 = 'player one'
P2 = 'player two'
P1_WINS = 'player one wins'
P2_WINS = 'player two wins'
TIE = 'tie game'

# The constant describing which puzzle to play. Replace the 'puzzle1.txt' with
# any other puzzle file (e.g., 'puzzle2.txt') to play a different game.
PUZZLE_FILE = 'puzzle1.txt'


# Helper functions.  Do not modify these, although you are welcome to
# call them.

def get_column(puzzle: str, col_num: int) -> str:
    """Return column col_num of puzzle.

    Precondition: 0 <= col_num < number of columns in puzzle

    >>> get_column('abcd\\nefgh\\nijkl\\n', 1)
    'bfj'
    """

    puzzle_list = puzzle.strip().split('\n')
    column = ''
    for row in puzzle_list:
        column += row[col_num]

    return column


def get_row_length(puzzle: str) -> int:
    """Return the length of a row in puzzle.
    """

    return len(puzzle.split('\n')[0])


def contains(text1: str, text2: str) -> bool:
    """Return whether text2 appears anywhere in text1.

    >>> contains('abc', 'bc')
    True
    >>> contains('abc', 'cb')
    False
    """

    return text2 in text1

def get_winner(score1: int, score2: int) -> str:
    """Return 'player one wins,' 'player two wins,'or 'tie game' depending on
    'score1' and 'score2'

    >>>get_winner(1,2)
    'player two wins'
    >>>get_winner(2,1)
    'player one wins'
    >>>get_winner(1,1)
    'tie game'
    """

    if score1 > score2:
        return P1_WINS
    elif score1 < score2:
        return P2_WINS
    else:
        return TIE

def reverse(rvrs: str) -> str:
    """Return the reverse of rvrs

    >>>reverse('hi')
    'ih'
    >>>reverse('player one')
    'eno reyalp'
    """

    return rvrs[::-1]

def get_row(puzzle: str, row_num: int) -> str:
    """Return the letters in a row depending on whether it's in the puzzle and
    its row_num

    Precondition: the first row is row number 0

    >>>get_row('abcd\nefgh\nijkl\n', 2)
    ijkl
    >>>get_row('abcd\nefgh\nijkl\n', 1)
    efgh
    """

    row_value = (get_row_length(puzzle) + 1) * row_num

    return puzzle[row_value: row_value + get_row_length(puzzle)]


def get_factor(direction: str) -> int:
    """Return the multiplicative factor of a direction

    Preconditions: directions inputted must be 'up', 'down', 'forward', or
    'backward'

    >>>get_factor('up')
    4
    >>>get_factor('down')
    2
    """

    if direction == UP:
        return UP_FACTOR
    elif direction == DOWN:
        return DOWN_FACTOR
    elif direction == FORWARD:
        return FORWARD_FACTOR
    else:
        return BACKWARD_FACTOR

def get_points(direction: str, num_words_left: int) -> int:
    """Return different amounts of points depending on the direction given
    num_words_left

    Preconditions: num_words_left > 0

    >>>get_points('up', 2)
    32
    >>>get_points('down', 7)
    10
    >>>get_points('forward', 1)
    21
    """

    if num_words_left >= THRESHOLD:
        return get_factor(direction) * THRESHOLD
    elif 1 < num_words_left < THRESHOLD:
        return ((2 * THRESHOLD) - num_words_left) * get_factor(direction)
    else:
        return (2 * THRESHOLD - 1) * get_factor(direction) + BONUS

def check_guess(puzzle: str, direction: str, guess_word: str, row_col_num: int,
                num_words_left: int) -> int:
    """Return score depending on direction, row_col_num, and num_words_left and
    if guess_word is found in puzzle

    >>>check_guess('abcd\nefgh\nijkl\n', 'forward', 'ef', 1, 4)
    6
    >>>check_guess('abcd\nefgh\nijkl\n', 'up', 'jfb', 1, 1)
    48
    """

    if direction == FORWARD:
        word = get_row(puzzle, row_col_num)
    elif direction == BACKWARD:
        word = reverse(get_row(puzzle, row_col_num))
    elif direction == DOWN:
        word = get_column(puzzle, row_col_num)
    elif direction == UP:
        word = reverse(get_column(puzzle, row_col_num))
    else:
        word = ''

    if contains(word, guess_word):
        score = get_points(direction, num_words_left)
    score = 0

    return score

def get_current_player(player_one_turn: bool) -> str:
    """Return 'player one' iff player_one_turn is True; otherwise, return
    'player two'

    >>>get_current_player(True)
    'player one'
    >>>get_current_player(False)
    'player two'
    """

    if player_one_turn:
        return 'player one'
    return 'player two'
